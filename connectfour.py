import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COL_COUNT = 7


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)



#create a basic NumPy 6*7 connectfour board
def create_board():
	board = np.zeros((ROW_COUNT,COL_COUNT))
	return board
game_over = False
turn = 0

#check whether the last row in the specific column is empty or not
def is_valid_location(board,col):
	return board[ROW_COUNT - 1][col]==0

#return the next empty row in the specific column
def get_next_open_row(board,col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r
def flip_board(board):
	print(np.flip(board,0))

#Let's see who wins
def winning_move(board,piece):

    #first lets see horizontally
	for c in range(COL_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2]==piece and board[r][c+3]==piece:
				return True
    
    #check vertically
	for c in range(COL_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
				return True


	#check positively sloped diagnols
	for c in range(COL_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
				return True

	#check negatively sloped diagnols			
	for c in range(COL_COUNT-3):
		for r in range(3,ROW_COUNT):
			if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
				return True	
    			
    		
    		
#drop the piece in the specific column
def drop_piece(board,row,col,piece):
	board[row][col] = piece


#lets give some graphics to our basic board
def draw_board(board):
	for c in range(COL_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
			pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE + SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),radius)

	for c in range(COL_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c]==1:
				pygame.draw.circle(screen,RED,(int(c*SQUARESIZE + SQUARESIZE/2),height - int(r*SQUARESIZE+SQUARESIZE/2)),radius)
			elif board[r][c] == 2:
				pygame.draw.circle(screen,YELLOW,(int(c*SQUARESIZE + SQUARESIZE/2),height - int(r*SQUARESIZE+SQUARESIZE/2)),radius)
				


	pygame.display.update()			

				

			
			

board = create_board()
flip_board(board)

pygame.init()


SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width,height)
#radius of circles
radius  = int(SQUARESIZE/2 - 5)
#pygame docs
screen = pygame.display.set_mode(size)


draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace" , 75)

#lets play one round
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),radius)
			elif turn == 1:
				pygame.draw.circle(screen,YELLOW,(posx,int(SQUARESIZE/2)),radius)
		pygame.display.update()		
				
			
			

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))

		
			#ask for player 1 input
			if turn ==0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))
				if is_valid_location(board,col):
					row = get_next_open_row(board,col)
					drop_piece(board,row,col,1)
					if winning_move(board,1):
						label = myfont.render("Player 1 wins",1,RED)
						screen.blit(label,(50,10))
						game_over= True
						
						
			



            #player 2 input
			else:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))
				if is_valid_location(board,col):
					row = get_next_open_row(board,col)
					drop_piece(board,row,col,2)
					if winning_move(board,2):
						label = myfont.render("PLayer 2 wins",2,YELLOW)
						screen.blit(label,(50,10))
						game_over = True
						
						
            #the piece must go at the bottom
			flip_board(board)
			
			
			draw_board(board)

			turn = turn + 1
			turn = turn %2			


			if game_over:
				pygame.time.wait(2000)

