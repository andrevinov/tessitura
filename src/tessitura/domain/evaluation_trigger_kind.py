from enum import Enum


class EvaluationTriggerKind(Enum):
    INITIAL_EVALUATION = "initial_evaluation"
    TIME_THRESHOLD_REACHED = "time_threshold_reached"
    LEVEL_THRESHOLD_REACHED = "level_threshold_reached"
    ANCHOR_STATE_CHANGED = "anchor_state_changed"
    KNOWLEDGE_CHANGED = "knowledge_changed"
