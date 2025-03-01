# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command group for Config Management Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base as calliope_base


@calliope_base.ReleaseTracks(
    calliope_base.ReleaseTrack.ALPHA, calliope_base.ReleaseTrack.BETA
)
class Configmanagement(calliope_base.Group):
  """Manage Config Management feature.

  Manage Config Sync using the Config Management feature. Policy Controller
  users should use the separate command group: `gcloud container fleet
  policycontroller`. Hierarchy Controller users should use
  https://github.com/kubernetes-sigs/hierarchical-namespaces instead.
  """

  category = calliope_base.COMPUTE_CATEGORY
