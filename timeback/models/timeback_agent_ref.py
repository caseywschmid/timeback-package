from pydantic import BaseModel, Field
from timeback.enums.timeback_agent_type import TimebackAgentType


class TimebackAgentRef(BaseModel):
    """Agent reference with limited types.
    
    Represents a reference to an agent (student, user, or parent).
    Used in user models to specify agent relationships.
    """

    sourcedId: str = Field(..., description="Unique identifier of the agent")
    type: TimebackAgentType = Field(..., description="Type of agent reference. See TimebackAgentType enum.")
