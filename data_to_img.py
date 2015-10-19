import Image
import numpy as np

cont = True;
times = 0;
while (cont):
    w,h = 96,96;
    data = np.zeros( (w,h,3), dtype=np.uint8)
    if (times == 0):
        print "Welcome!";
    print " Which dataset do you want to select?";
    print " You have 2 options: train or test";
    first = str(raw_input(" Please type 'train' or 'test', or 'cancel' to cancel: "));
    if (first == 'cancel'):
        print "Have a good day!";
        break;
    if (first == 'train'):
        Data = np.loadtxt('trainData.csv', delimiter=',');
        right = False;
        n = Data.shape[0];
        while (right == False):
            print "  trainData has " + str(n) + " entries";
            second = int(raw_input("  Please enter the number of the entry ([1," + str(n) + "]) you want to see: "));
            if (second > n):
                print "  This entry does not exist, please enter correct entry";
                right = False;
            else:
                right = True;
        Data = Data[second];
        r, g, b = 0,0,0;
        print " What color do you want to choose for background?";
        fourth = str(raw_input(" You have 3 options: r for red, g for green, b for blue: "));
        if (fourth == 'r'):
            r = 1;
        else:
            if (fourth == 'g'):
                g = 1;
            else:
                b = 1;
        for i in range(w):
            for j in range(h):
                data[i,j] = [int(Data[j+i*h])*r,int(Data[j+i*h])*g,int(Data[j+i*h])*b];
        img = Image.fromarray(data, 'RGB')
        img.save('train_'+str(second)+'.png')
        img.show();
    if (first == 'test'):
        Data = np.loadtxt('testData.csv', delimiter=',');
        right = False;
        n = Data.shape[0];
        while (right == False):
            print "  testData has " + str(n) + " entries";
            second = int(raw_input("  Please enter the number of the entry ([1," + str(n) + "]) you want to see: "));
            if (second > n):
                print "  This entry does not exist, please enter correct entry";
                right = False;
            else:
                right = True;
        Data = Data[second];
        r, g, b = 0,0,0;
        print " What color do you want to choose for background?";
        fourth = str(raw_input(" You have 3 options: r for red, g for green, b for blue: "));
        if (fourth == 'r'):
            r = 1;
        else:
            if (fourth == 'g'):
                g = 1;
            else:
                b = 1;
        for i in range(w):
            for j in range(h):
                data[i,j] = [int(Data[j+i*h])*r,int(Data[j+i*h])*g,int(Data[j+i*h])*b];
        img = Image.fromarray(data, 'RGB')
        img.save('test_'+str(second)+'.png')
        img.show();
    third = str(raw_input(" Do you want to repeat?(yes/no): "));
    if (third == "Yes" or third == "yes"):
        times += 1;
        cont = True;
    else:
        print "Have a good day!";
        break;