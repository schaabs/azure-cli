# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ..rule_decorators import parameter_rule, exclude_from_ci
from ..linter import RuleError


@exclude_from_ci
@parameter_rule
def missing_parameter_help_rule(linter, command_name, parameter_name):
    if not linter.get_parameter_help(command_name, parameter_name):
        raise RuleError('Missing help')
