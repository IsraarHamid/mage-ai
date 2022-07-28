{% extends "transformers/transformer_actions/action.jinja" %}
{% block action %}
    """
    Execute Transformer Action: ActionType.DROP_DUPLICATE
    """
    action = build_transformer_action(
        df,
        action_type=ActionType.DROP_DUPLICATE,
        arguments=df.columns,  # Specify columns to use when comparing duplicates
        axis=Axis.ROW,
        options={'keep': 'first'},  # Specify whether to keep 'first' or 'last' duplicate
    )
{% endblock %}
