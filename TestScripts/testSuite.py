from unittest import TestLoader, TestSuite, TextTestRunner

from UnitTest_VolunteerRegister import MCGB_Test1
from UnitTest_VolunteerEventRegister import MCGB_Test6
from UnitTest_Login import MCGB_Test3
from UnitTest_Logout import MCGB_Test4
from UnitTest_OrganizationRegister import MCGB_Test2
from UnitTest_PostNewEvent import MCGB_Test5
from UnitTest_OrganizationDashboard import MCGB_Test7
from UnitTest_MarkAttendance import MCGB_Test8
from UnitTest_VolunteerMyEvent import MCGB_Test9
from UnitTest_VolunteerEditProfile import MCGB_Test10
from UnitTest_API import MCGB_Test11



if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MCGB_Test1),
        loader.loadTestsFromTestCase(MCGB_Test2),
        loader.loadTestsFromTestCase(MCGB_Test3),
        loader.loadTestsFromTestCase(MCGB_Test4),
        loader.loadTestsFromTestCase(MCGB_Test5),
        loader.loadTestsFromTestCase(MCGB_Test6),
        loader.loadTestsFromTestCase(MCGB_Test7),
        loader.loadTestsFromTestCase(MCGB_Test8),
        loader.loadTestsFromTestCase(MCGB_Test9),
        loader.loadTestsFromTestCase(MCGB_Test10),
        loader.loadTestsFromTestCase(MCGB_Test11),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)