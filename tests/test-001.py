# Copyright 2013 Fredrik Brannbacka
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import logworm

def callback(value, mode="append"):
    print mode, value

def line(line):
    print line
    
def test():
    parser = logworm.Worm(['default', 'arnold', 'non_existing'], callback, line)
    subprocess.Popen(['/Users/fredrik/Documents/workspace/logworm/tests/fake_scripts/dummy.sh', 'arnold'], 
                     stdout=parser.logpipe, stderr=parser.logpipe)
    
if __name__ == '__main__':
    test()