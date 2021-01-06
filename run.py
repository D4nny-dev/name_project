import astroFile as ast 
# from astroImages import * 

def main():

    
    t = ast.AstroFile("./images/sectork19/200712.png")
    dimension = t.get_dimencions("./images/sectork20/200621.png")
    print(dimension)



if __name__ == '__main__':
    main()