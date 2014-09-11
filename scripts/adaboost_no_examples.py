"""
this script plots training and testing accuracy of adaboost with number of training
examples.
"""

#global imports
import matplotlib.pyplot as plt
import time

#local imports
from pbtspot import set_default,adaboost_train_test, globalconstants
from pbtspot.adaboost.generateimage import vid_utils


set_default.set_default_constants();
def init_set(glob_const):
    
    #set constants
    glob_const.no_pos_training_eg=100;
    glob_const.no_neg_training_eg=100;
    glob_const.no_pos_testing_eg=1000;
    glob_const.no_neg_testing_eg=1000;
    glob_const.savefile();



def exampleno_script():
    glob_const=globalconstants.GlobalConstants();
    init_set(glob_const);
    SNRval=0.5;

    #exampleno_list=[];
    exampleno_list=range(50,1000,50);
    training_acc=[];
    testing_acc=[];
    list_tillnow=[];
    time_list=[];
    
    training_rounds=15;
    pos_te_eg=glob_const.no_pos_testing_eg;
    neg_te_eg=glob_const.no_neg_testing_eg;
    
    for exampleno in exampleno_list:
        starttime=time.time();
        
        glob_const.no_pos_training_eg=exampleno;
        glob_const.no_neg_training_eg=exampleno;
        glob_const.savefile();
        
        boost=adaboost_train_test.AdaBoostTrainTest(SNRval,training_rounds,\
              exampleno,exampleno,pos_te_eg,neg_te_eg);
        boost.train_adaboost();
        boost.test_adaboost();
        elapsed=time.time()-starttime;
        
        #append values
        training_acc.append(boost.training_accuracy);
        testing_acc.append(boost.testing_accuracy);
        list_tillnow.append(exampleno);
        time_list.append(elapsed)
        vid_utils.savefile(list_tillnow,training_acc,\
                           'data/training_acc_eg.txt')
        vid_utils.savefile(list_tillnow,testing_acc,\
                'data/testing_acc_eg.txt')
        vid_utils.savefile(list_tillnow,time_list,\
                'data/time_vals.txt')

    plt.plot(exampleno_list,training_acc,'bo-',label='Training Accuracy');
    plt.plot(exampleno_list,testing_acc,'ro-',label='Testing Accuracy');
    plt.legend();
    plt.show();


if __name__=="__main__":
    exampleno_script()