# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2018
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

import pixiedust_rosie.classify.classify_data as cd
import pixiedust
from pixiedust.display.app import *
from pixiedust.utils.shellAccess import ShellAccess

@PixieApp
class PixieRosieApp:

    def setup(self):
        self.schema = cd.Schema(self.pixieapp_entity, 50)

    def textToInt(self,text):
        return int(text)

    @route()
    def main(self):
        return self.env.getTemplate("main_screen_ui.html")

    @route(modify="*")
    def modify_screen(self, modify):
        return self.env.getTemplate("modify_screen.html")

    @route(transform="*")
    def transform_screen(self, transform):
        return self.env.getTemplate("transform_screen.html")