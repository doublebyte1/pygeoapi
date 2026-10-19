# ****************************** -*-
# flake8: noqa
# =================================================================
#
# Authors: Francesco Bartoli <xbartolone@gmail.com>
#
# Copyright (c) 2022 Francesco Bartoli
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

from enum import Enum

from pydantic import BaseModel


class SupportedFormats(Enum):
    JSON = "json"
    YAML = "yaml"


class OAPIFormat(BaseModel):
    __root__: SupportedFormats = SupportedFormats.YAML
# Authors: Francesco Bartoli <xbartolone@gmail.com>
# Copyright (c) 2022 Francesco Bartoli
import io
from pathlib import Path
from typing import Union
from pygeoapi.models.openapi import OAPIFormat
def generate_openapi_document(cfg_file: Union[Path, io.TextIOWrapper],
                              output_format: OAPIFormat):
    """
    Generate an OpenAPI document from the configuration file

    :param cfg_file: configuration Path instance
    :param output_format: output format for OpenAPI document

    :returns: content of the OpenAPI document in the output
              format requested
    """
    if isinstance(cfg_file, Path):
        with cfg_file.open(mode="r") as cf:
            s = yaml_load(cf)
    else:
        s = yaml_load(cfg_file)
    pretty_print = s['server'].get('pretty_print', False)

    if output_format == 'yaml':
        content = yaml.safe_dump(get_oas(s), default_flow_style=False)
    else:
        content = to_json(get_oas(s), pretty=pretty_print)
    return content


    content = generate_openapi_document(config_file, format_)