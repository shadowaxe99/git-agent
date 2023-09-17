```python
import json

# Shared dependencies
from requirements_gathering import user_requirements
from implementation import integrated_system
from user_validation import user_feedback

# Data schemas
from schemas import DocumentationSchema

# Message names
from messages import FinalizationMessage

final_documentation = {}

def finalize_integration():
    """
    Finalize the integration and document the changes made during the integration.
    """
    global final_documentation
    final_documentation = {
        "user_requirements": user_requirements,
        "integrated_system": integrated_system,
        "user_feedback": user_feedback
    }

    # Validate final documentation with schema
    doc_schema = DocumentationSchema()
    if not doc_schema.validate(final_documentation):
        raise Exception(FinalizationMessage.DOCUMENTATION_VALIDATION_ERROR)

    # Save final documentation as a JSON file
    with open('final_documentation.json', 'w') as file:
        json.dump(final_documentation, file)

    print(FinalizationMessage.FINALIZATION_SUCCESS)

def provide_documentation():
    """
    Provide documentation on how to use the integrated system.
    """
    print(FinalizationMessage.DOCUMENTATION_PROVIDED)

def handover_system():
    """
    Handover the integrated system to the user.
    """
    print(FinalizationMessage.SYSTEM_HANDED_OVER)

if __name__ == "__main__":
    finalize_integration()
    provide_documentation()
    handover_system()
```