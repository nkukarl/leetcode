from unittest import TestCase

from count_and_say import Solution


class TestCountAndSay(TestCase):
    def test_count_and_say(self):
        # Setup
        sol = Solution()
        DICT = {
            1: '1',
            2: '11',
            3: '21',
            4: '1211',
            5: '111221',
            6: '312211',
            7: '13112221',
            8: '1113213211',
            20: '11131221131211132221232112111312111213111213211231132132211211'
                '13122113121122132112311321322112311311222113111231133221121113'
                '12211312111322111213122112311311123112112322211213211321322113'
                '31121321231231121113112221121321133112132112312321123113112221'
                '121113122113121113123112112322111213211322211312113211',
        }

        # Exercise and Verify
        for n, expected_ans in DICT.items():
            ans = sol.count_and_say(n)
            self.assertEqual(ans, expected_ans)
