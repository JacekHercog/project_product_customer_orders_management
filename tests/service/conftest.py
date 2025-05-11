from unittest.mock import MagicMock
from src.repository import PurchaseSummaryRepository
from src.service import PurchasesSummaryService
import pytest

@pytest.fixture
def mock_repository() -> MagicMock:
    """
    Fixture for mocking the PurchaseSummaryRepository.

    Returns:
        MagicMock: A mock object for the PurchaseSummaryRepository.
    """
    return MagicMock()

@pytest.fixture
def service(mock_repository: MagicMock) -> PurchasesSummaryService:
    """
    Fixture for creating an instance of PurchasesSummaryService.

    Args:
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Returns:
        PurchasesSummaryService: An instance of the PurchasesSummaryService with a mocked repository.
    """
    return PurchasesSummaryService(repository=mock_repository)