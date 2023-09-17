```python
# Importing necessary libraries
import git
from sonarqube import SonarQubeClient
from jira import JIRA

# Defining the tools and technologies
class ToolsAndTechnologies:
    def __init__(self):
        self.programming_languages = None
        self.version_control = None
        self.code_analysis_tool = None
        self.project_management_tool = None

    # Function to set the programming languages used in the repositories
    def set_programming_languages(self, languages):
        self.programming_languages = languages

    # Function to set the version control system
    def set_version_control(self, version_control):
        self.version_control = version_control

    # Function to set the code analysis tool
    def set_code_analysis_tool(self, code_analysis_tool):
        self.code_analysis_tool = code_analysis_tool

    # Function to set the project management tool
    def set_project_management_tool(self, project_management_tool):
        self.project_management_tool = project_management_tool

    # Function to get the programming languages used in the repositories
    def get_programming_languages(self):
        return self.programming_languages

    # Function to get the version control system
    def get_version_control(self):
        return self.version_control

    # Function to get the code analysis tool
    def get_code_analysis_tool(self):
        return self.code_analysis_tool

    # Function to get the project management tool
    def get_project_management_tool(self):
        return self.project_management_tool

# Creating an instance of the ToolsAndTechnologies class
tools_and_technologies = ToolsAndTechnologies()

# Setting the tools and technologies
tools_and_technologies.set_programming_languages(['Python', 'JavaScript'])
tools_and_technologies.set_version_control(git.Git())
tools_and_technologies.set_code_analysis_tool(SonarQubeClient(url="http://localhost:9000"))
tools_and_technologies.set_project_management_tool(JIRA(server='https://your_jira_server'))
```
