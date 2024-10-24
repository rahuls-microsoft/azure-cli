# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core import AzCommandsLoader
from ._client_factory import cf_computefleet
from azure.cli.command_modules.mymod._help import helps  # pylint: disable=unused-import

class ComputeFleetCommandsLoader(AzCommandsLoader):

    def load_command_table(self, args):
        from azure.cli.core.commands import CliCommandType
      
        computefleet_custom = CliCommandType(
          operations_tmpl='azure.mgmt.computefleet.operations#MyModOperations.{}',
      )

        with self.command_group('computefleet', computefleet_custom, client_factory=cf_computefleet) as g:
            g.command('create', 'create_computefleet')
            g.command('update', 'update_computefleet')
            g.command('delete', 'delete_computefleet')
            g.command('list', 'list_computefleets')
            g.command('show', 'show_computefleet')