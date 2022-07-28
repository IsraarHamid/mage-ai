{% extends "transformers/transformer_actions/action.jinja" %}
{% block action %}
    """
    Execute Transformer Action: ActionType.FIRST
    """
    action = build_transformer_action(
        df,
        action_type=ActionType.FIRST,
        action_code='',  # Enter filtering condition on rows before aggregation
        arguments=[],  # Enter the columns to compute aggregate over
        axis=Axis.COLUMN,
        options={'groupby_columns': []},  # Enter columns to group by
        outputs=[
            # The number of outputs below must match the number of arguments
            {'uuid': 'new_aggregate_column_1', 'column_type': 'category'},
            {'uuid': 'new_aggregate_column_2', 'column_type': 'number'},
        ],
    )
{% endblock %}
