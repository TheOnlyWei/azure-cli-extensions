from azure.cli.core import AzCommandsLoader
from azure.cli.core.profiles import register_resource_type
from azure.cli.core.commands import AzCommandGroup, AzArgumentContext

import azext_arca_extension._help  # pylint: disable=unused-import
from .profiles import K8S_CONFIGURATION
from azure.cli.core import get_default_cli
import subprocess
import json

def showtipsurl():
    #out = subprocess.run(['az','extension', 'list-available', '--output', 'table'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #print("Out value: @{}@".format(out))
    get_default_cli().invoke(['extension', 'list-available', '--output', 'table'])
    print('Azure Tips and Tricks - The Complete List: tip-complete-list/')

class ArcAExtensionCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType

        # register_resource_type('latest', K8S_CONFIGURATION, '2022-05-06')
        
        custom_type = CliCommandType(operations_tmpl='azext_arca_extension#{}')
        super(ArcAExtensionCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=custom_type)

    def load_command_table(self, args):
        with self.command_group('gimme') as g:
            g.custom_command('tips', 'showtipsurl')
        return self.command_table

    def load_arguments(self, _):
        pass

COMMAND_LOADER_CLS = ArcAExtensionCommandsLoader