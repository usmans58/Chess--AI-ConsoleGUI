from __future__ import annotations

import argparse
import random
import sys
from typing import Optional

from AI import AI
from Board import Board
from InputParser import InputParser
from Move import Move
from Piece import Piece

WHITE = True
BLACK = False

def printCommandOptions() -> None:
    printLegalMovesOption = 'l : show all legal moves'
    randomMoveOption = 'r : make a random move'
    quitOption = 'quit/exit : resign'
    moveOption = 'a3, Nc3, Qxa8 etc'
    options = [
        printLegalMovesOption,
        randomMoveOption,
        quitOption,
        moveOption,
        '',
    ]
    print('\n'.join(options))


def printAllLegalMoves(board: Board, parser: InputParser) -> None:
    for move in parser.getLegalMovesWithNotation(
        board.currentSide, short=True
    ):
        print(move.notation)


def getRandomMove(board: Board, parser: InputParser) -> Move:
    legalMoves = board.getAllMovesLegal(board.currentSide)
    randomMove = random.choice(legalMoves)
    randomMove.notation = parser.notationForMove(randomMove)
    return randomMove


def printBoard(board: Board):
    print()
    print(board)
    print()


def printGameMoves(history: list[tuple[Move, Optional[Piece]]]) -> None:
    counter = 0
    for num, mv in enumerate(history):
        if num % 2 == 0:
            if counter % 6 == 0:
                print()
            print(f'{counter + 1}.', end=' ')
            counter += 1

        print(mv[0].notation, end=' ')
    print()


def startGame(board: Board, playerSide: bool, ai: AI) -> None:
    parser = InputParser(board, playerSide)
    while True:
        if board.isCheckmate():
            if board.currentSide == playerSide:
                print('Checkmate, you lost')
            else:
                print('Checkmate! You won!')
            printGameMoves(board.history)
            return

        if board.isStalemate():
            print('Stalemate')
            printGameMoves(board.history)
            return

        if board.noMatingMaterial():
            print('Draw due to no mating material')
            printGameMoves(board.history)
            return

        if board.currentSide == playerSide:
            move = None
            command = input("It's your move.")
            if command.lower() == '?':
                printCommandOptions()
                continue
            elif command.lower() == 'l':
                printAllLegalMoves(board, parser)
                continue
            elif command.lower() == 'r':
                move = getRandomMove(board, parser)
            elif command.lower() == 'exit' or command.lower() == 'quit':
                return
            
            try:
                if move is None:
                    move = parser.parse(command)
            except ValueError as error:
                print('%s' % error)
                continue
            print(move.piece)
            board.makeMove(move)
            printBoard(board)

        else:
            print('AI thinking...')
            move = ai.getBestMove()
            move.notation = parser.notationForMove(move)
            board.makeMove(move)
            printBoard(board)

board = Board()
def main():
    
    print('Welcome to Chess!')
    playerSide = WHITE
    playerChoiceInput = input(
        'What side would you like to play as [White:w/Black:b]? '
    ).lower()
    if 'w' in playerChoiceInput:
        print('YYou have chosen to play as white')
        playerSide= WHITE
    else:
        print('You have chosen to play as black')
        playerSide = BLACK
    
    board.currentSide = WHITE
    print()
    
    depthInput = 2
    depthInput = int(input('How deep should the AI look for moves?\n'))
    while depthInput <= 0:
        depthInput = int(input('How deep should the AI look for moves?\n''Your input must be above 0.'))
    aiDepth = depthInput
    opponentAI = AI(board, not playerSide, aiDepth)
    printBoard(board)
    startGame(board, playerSide, opponentAI)
   

if __name__ == '__main__':
    main()
