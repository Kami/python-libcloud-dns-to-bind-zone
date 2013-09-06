# Licensed to Tomaz Muraus under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# Tomaz muraus licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from libcloud.dns.types import Provider
from libcloud.dns.providers import get_driver

from libcloud_to_bind import libcloud_zone_to_bind_zone_file


DOMAIN_TO_EXPORT = 'example.com'

Zerigo = get_driver(Provider.ZERIGO)
driver = Zerigo('email', 'api key')

zones = driver.list_zones()
zone = [z for z in zones if z.domain == DOMAIN_TO_EXPORT][0]

result = libcloud_zone_to_bind_zone_file(zone=zone)
print(result)
