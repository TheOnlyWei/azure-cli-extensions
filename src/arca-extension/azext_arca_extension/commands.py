# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType
from azure.cli.core.commands.arm import show_exception_handler
from .profiles import K8S_CONFIGURATION


def load_command_table(self, _):  # pylint: disable=too-many-locals, too-many-statements

    def get_custom_sdk(custom_module, client_factory, resource_type=K8S_CONFIGURATION):
        """Returns a CliCommandType instance with specified operation template based on the given custom module name.
        This is useful when the command is not defined in the default 'custom' module but instead in a module under
        'operations' package."""
        return CliCommandType(
            operations_tmpl='azext_storage_preview.operations.{}#'.format(custom_module) + '{}',
            client_factory=client_factory,
            resource_type=resource_type
        )

    storage_account_sdk = CliCommandType(
        operations_tmpl='azext_storage_preview.vendored_sdks.azure_mgmt_storage.operations#'
                        'StorageAccountsOperations.{}',
        client_factory=cf_sa,
        resource_type=K8S_CONFIGURATION
    )

    storage_account_custom_type = CliCommandType(
        operations_tmpl='azext_storage_preview.operations.account#{}',
        client_factory=cf_sa,
        resource_type=K8S_CONFIGURATION
    )

    with self.command_group('storage account', storage_account_sdk, resource_type=CUSTOM_MGMT_STORAGE,
                            custom_command_type=storage_account_custom_type) as g:
        g.custom_command('create', 'create_storage_account')
        g.generic_update_command('update', getter_name='get_properties', setter_name='update',
                                 custom_func_name='update_storage_account')