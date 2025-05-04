from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseLanguageModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from agent_tools.duckduckgo_search import search_tool
from agent_tools.save_to_txt import save_tool
from agent_tools.wikipedia_query import wiki_tool
from dto.research_response import ResearchResponse


class Agent:

    load_dotenv()
    __default_prompt: str = """You are a research assistant that will help generate a research paper.
    Answer the user query and use necessary tools.
    Wrap the output in this format and provide no other text
    After it save the output to a text file."""

    __llm_openAI: BaseLanguageModel = ChatOpenAI(model="gpt-4o-mini")
    __llm_claude = ChatAnthropic(model="claude-3-5-sonnet-20241022")

    def __init__(self, system_prompt: str = __default_prompt, tools=None):
        if tools is None:
            tools = list()
        # load_dotenv()
        self.__system_prompt = system_prompt
        self.__parser = PydanticOutputParser(pydantic_object=ResearchResponse)
        self.__tools = [search_tool, wiki_tool, save_tool] + tools
        self.__prompt = self.__create_prompt()
        self.__agent = self.__create_agent(llm=self.__llm_openAI, prompt=self.__prompt)

    def __create_prompt(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages(
            [
                ("system",
                 self.__system_prompt + "\n{format_instructions}"),
                ("placeholder", "{chat_history}"),
                ("human", "{query}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        ).partial(format_instructions=self.__parser.get_format_instructions())

    def __create_agent(self, llm: BaseLanguageModel, prompt: ChatPromptTemplate) -> AgentExecutor:
        agent = create_tool_calling_agent(
            llm=llm,
            prompt=prompt,
            tools=self.__tools,
        )
        agent_executor = AgentExecutor(agent=agent, tools=self.__tools, verbose=True)
        return agent_executor

    def execute_query(self, query: str):
        raw_response = self.__agent.invoke({"query": query})
        print(raw_response)
        structured_response: ResearchResponse = self.__parser.parse(raw_response.get("output"))
        return structured_response
