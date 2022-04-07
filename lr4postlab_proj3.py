#FONSECA, ROBNE KYLE (LAYGO)
#GOPOLE, KHYLE MATTHEW (PABLO)
#CPE106L-B1 - GROUP 3
#LABORATORY 4 (POST-LAB PROBLEM 3)

"""
3. Create a unit test program for testing  the Tic Tac Toe Console App
"""
import unittest 
import oxo_dialog_ui
import oxo_logic

class TestOxo(unittest.TestCase):
    def testStartGame(self):
        self.assertEqual(oxo_dialog_ui.startGame(), list(" "*9))


    def testResumeGame(self):
        self.assertEqual(oxo_dialog_ui.resumeGame(), oxo_logic.restoreGame())


    def testQuitGame(self):
        self.assertRaises(SystemExit, oxo_dialog_ui.quit)

if __name__=='__main__':
    unittest.main()

