from eval import score
from hmm import main

if __name__ == "__main__":
    main()
    score("WSJ/WSJ_24.pos", "output/wsj_24.pos")