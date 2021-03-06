from typing import List

from catalyst.callbacks.metric import LoaderMetricCallback
from catalyst.metrics.functional import (
    wrap_class_metric2dict,
    wrap_metric_fn_with_activation,
)
from catalyst.metrics.precision import average_precision


class AveragePrecisionCallback(LoaderMetricCallback):
    """AveragePrecision metric callback."""

    def __init__(
        self,
        input_key: str = "targets",
        output_key: str = "logits",
        prefix: str = "average_precision",
        activation: str = "Sigmoid",
        class_args: List[str] = None,
        **kwargs,
    ):
        """
        Args:
            input_key: input key to use for
                calculation mean average precision;
                specifies our `y_true`.
            output_key: output key to use for
                calculation mean average precision;
                specifies our `y_pred`.
            prefix: key for the metric's name
            activation: An torch.nn activation applied to the outputs.
                Must be one of ``'none'``, ``'Sigmoid'``, or ``'Softmax'``
            class_args: class names to display in the logs.
                If None, defaults to indices for each class, starting from 0
        """
        metric_fn = wrap_metric_fn_with_activation(
            metric_fn=average_precision, activation=activation
        )
        metric_fn = wrap_class_metric2dict(metric_fn, class_args=class_args)
        super().__init__(
            prefix=prefix,
            metric_fn=metric_fn,
            input_key=input_key,
            output_key=output_key,
            **kwargs,
        )


__all__ = ["AveragePrecisionCallback"]
