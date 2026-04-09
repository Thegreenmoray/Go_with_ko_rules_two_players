import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest

import Go
import Rules
import Player
import Actualgame
import testgo
import main


class MyTestCase(unittest.TestCase):
    def test_outof_bounds(self):
        board=Go.createboard()
        self.assertTrue(Rules.is_out_of_bounds(board,20,20))
        self.assertFalse(Rules.is_out_of_bounds(board,10,10))
    def test_ko(self):
        board=Go.createboard(2)
        board2=Go.createboard(2)
        self.assertTrue(Rules.ko_check(board,board2))
        board2[0][1] = 'X'
        self.assertFalse(Rules.ko_check(board,board2))
    def test_copy_board(self):
        board=Go.createboard()
        copy_of_board= Rules.copy_board(board)
        self.assertEqual(board,copy_of_board)
    def test_is_surrounded(self):
        board=Go.createboard(4)
        board[2][0]='X'
        board[2][1]='O'
        board[2][2]='X'
        board[1][1]='X'
        board[3][1]='X'
        issurron=Rules.hasliberties(board,2,1,'O','X',len(board))
        self.assertTrue(issurron)
    def test_is_capturing(self):
        board = Go.createboard(4)
        board[2][0] = 'X'
        board[2][1] = 'O'
        board[2][2] = 'X'
        board[1][1] = 'X'
        board[3][1] = 'X'
        issurron = Rules.iscapturing(board, 2, 2, 'X', 'O', len(board))
        self.assertTrue(issurron)
    def test_removestone(self):
        board = Go.createboard(4)
        board[2][0] = 'X'
        board[2][2] = 'X'
        board[1][1] = 'X'
        board[3][1] = 'X'
        testboard=Go.createboard(4)
        testboard[2][0] = 'X'
        testboard[2][1] = 'O'
        testboard[2][2] = 'X'
        testboard[1][1] = 'X'
        testboard[3][1] = 'X'
        self.assertEqual(Rules.removestones(testboard,[(2,1)]),board)

    def test_blackplacement(self):
        board = Go.createboard(4)
        board[2][0] = 'X'
        board[2][1] = 'O'
        board[2][2] = ' '
        board[1][1] = 'X'
        board[3][1] = 'X'
        testboard,allowed=Rules.blackplace(board,2,2)
        board[2][1] = ' '
        board[2][2] = 'X'

        self.assertEqual(board,testboard)


if __name__ == '__main__':
    unittest.main()
