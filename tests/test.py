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

import sys

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from libcloud.dns.base import Zone, Record
from libcloud.dns.types import RecordType
from mock import Mock

from libcloud_to_bind import libcloud_zone_to_bind_zone_file

MOCK_RECORDS_VALUES = [
    {'id': 1, 'name': 'www', 'type': RecordType.A, 'data': '127.0.0.1'},
    {'id': 2, 'name': 'www', 'type': RecordType.AAAA,
     'data': '2a01:4f8:121:3121::2'},

    # Custom TTL
    {'id': 3, 'name': 'www', 'type': RecordType.A, 'data': '127.0.0.1',
     'extra': {'ttl': 123}},

    # Record without a name
    {'id': 4, 'name': '', 'type': RecordType.A,
     'data': '127.0.0.1'},

    {'id': 5, 'name': 'test1', 'type': RecordType.TXT,
     'data': 'test foo bar'},

    # TXT record with quotes
    {'id': 5, 'name': 'test2', 'type': RecordType.TXT,
     'data': 'test "foo" "bar"'},

    # Records with priority
    {'id': 5, 'name': '', 'type': RecordType.MX,
     'data': 'mx.example.com', 'extra': {'priority': 10}},
    {'id': 5, 'name': '', 'type': RecordType.SRV,
     'data': '10 3333 example.com', 'extra': {'priority': 20}},
]


class LibcloudZoneToBINDZoneTestCase(unittest.TestCase):
    def test_slave_should_throw(self):
        zone = Zone(id=1, domain='example.com', type='slave', ttl=900,
                    driver=None)
        self.assertRaises(ValueError, libcloud_zone_to_bind_zone_file, zone)

    def test_success(self):
        driver = Mock()
        zone = Zone(id=1, domain='example.com', type='master', ttl=900,
                    driver=driver)

        mock_records = []

        for values in MOCK_RECORDS_VALUES:
            values = values.copy()
            values['driver'] = driver
            values['zone'] = zone
            record = Record(**values)
            mock_records.append(record)

        driver.list_records.return_value = mock_records

        output = libcloud_zone_to_bind_zone_file(zone=zone)
        lines = output.split('\n')

        self.assertRegexpMatches(lines[1], r'\$ORIGIN example\.com\.')
        self.assertRegexpMatches(lines[2], r'\$TTL 900')

        self.assertRegexpMatches(lines[4], r'www.example.com\.\s+900\s+IN\s+A\s+127\.0\.0\.1')
        self.assertRegexpMatches(lines[5], r'www.example.com\.\s+900\s+IN\s+AAAA\s+2a01:4f8:121:3121::2')
        self.assertRegexpMatches(lines[6], r'www.example.com\.\s+123\s+IN\s+A\s+127\.0\.0\.1')
        self.assertRegexpMatches(lines[7], r'example.com\.\s+900\s+IN\s+A\s+127\.0\.0\.1')
        self.assertRegexpMatches(lines[8], r'test1.example.com\.\s+900\s+IN\s+TXT\s+"test foo bar"')
        self.assertRegexpMatches(lines[9], r'test2.example.com\.\s+900\s+IN\s+TXT\s+"test \\"foo\\" \\"bar\\""')
        self.assertRegexpMatches(lines[10], r'example.com\.\s+900\s+IN\s+MX\s+10\s+mx.example.com')
        self.assertRegexpMatches(lines[11], r'example.com\.\s+900\s+IN\s+SRV\s+20\s+10 3333 example.com')

if __name__ == '__main__':
    sys.exit(unittest.main())
