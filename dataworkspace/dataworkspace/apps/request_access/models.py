from django.conf import settings
from django.db import models

from dataworkspace.apps.core.models import (  # pylint: disable=import-error
    TimeStampedModel,
)
from dataworkspace.apps.core.storage import S3FileStorage


class AccessRequest(TimeStampedModel):

    JOURNEY_TOOLS_ACCESS = 'tools_access_only'
    JOURNEY_DATASET_ACCESS = 'dataset_access_only'
    JOURNEY_DATASET_AND_TOOLS_ACCESS = 'dataset_and_tools_access'

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='access_requests',
    )
    catalogue_item_id = models.UUIDField(null=True)
    contact_email = models.CharField(max_length=256, null=True, blank=False)
    reason_for_access = models.TextField(null=True, blank=False)
    training_screenshot = models.FileField(
        storage=S3FileStorage(location='training_screenshots'), null=True, blank=True,
    )
    spss_and_stata = models.BooleanField(default=False, blank=True)
    line_manager_email_address = models.CharField(max_length=256, null=True)
    reason_for_spss_and_stata = models.TextField(null=True)
    zendesk_reference_number = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f'{self.requester} - Zendesk reference number: {self.zendesk_reference_number}'

    @property
    def journey(self):
        if not self.catalogue_item_id:
            return self.JOURNEY_TOOLS_ACCESS
        elif not self.training_screenshot:
            return self.JOURNEY_DATASET_ACCESS
        else:
            return self.JOURNEY_DATASET_AND_TOOLS_ACCESS
