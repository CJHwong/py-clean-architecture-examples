from abc import ABC, abstractmethod


class ICalculatorPresenter(ABC):
    """
    An abstract boundary (interface) for the presenter.

    This interface is defined in the Use Cases layer and implemented by
    the Presenters in the Interface Adapters layer. It allows the use cases
    to pass data outwards without depending on any concrete presenter class,
    adhering to the Dependency Rule.
    """

    @abstractmethod
    def present_update(self, display_value: str):
        """Presents an update to the display."""
        pass
