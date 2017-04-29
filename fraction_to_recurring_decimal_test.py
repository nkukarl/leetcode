from unittest import TestCase

from nose_parameterized import parameterized

from fraction_to_recurring_decimal import Solution


class TestFractionToRecurringDecimal(TestCase):
    @parameterized.expand([
        [
            {
                'numerator': 1,
                'denominator': 4,
            },
            '0.25',
        ],
        [
            {
                'numerator': 1,
                'denominator': 6,
            },
            '0.1(6)',
        ],
        [
            {
                'numerator': 1,
                'denominator': 7,
            },
            '0.(142857)',
        ],
        [
            {
                'numerator': 1,
                'denominator': 998,
            },
            '0.0(01002004008016032064128256513026052104208416833667334669338677'
            '354709418837675350701402805611222444889779559118236472945891783567'
            '134268537074148296593186372745490981963927855711422845691382765531'
            '062124248496993987975951903807615230460921843687374749498997995991'
            '983967935871743486973947895791583166332665330661322645290581162324'
            '649298597194388777555110220440881763527054108216432865731462925851'
            '703406813627254509018036072144288577154308617234468937875751503006'
            '0120240480961923847695390781563126252505)'
        ],
        [
            {
                'numerator': 1,
                'denominator': 999,
            },
            '0.(001)',
        ]
    ])
    def test_fraction_to_decimal(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.fraction_to_decimal(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
