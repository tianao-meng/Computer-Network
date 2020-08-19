import numpy as np
import matplotlib.pyplot as plt
import copy
import random
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.cluster import OPTICS
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
import math

random.seed(0)
def benign_dataset():
    # each element in attribute_txt is a attribute list representing a sample
    attribute_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//benign_traffic-4.csv", delimiter=',', dtype=np.str)
    #print(len(attribute_csv))
    attribute = list(attribute_csv)
    #print ("attribute before: ",attribute[0][0])
    attribute = attribute[1:5001]
    #print ("attribute later: ", attribute[0][0])
    attribute = np.array(attribute,dtype=float)
    #attribute = attribute[:, :5000]
    print("len attribute in benigh: ", len(attribute))
    #attribute.astype("float32")

    label = []
    for i in range(len(attribute)):
        label.append('benign')

    #label_csv = np.array(label_csv)
    label = np.array(label)
    return attribute, label

def gafgyt_dataset():
    # each element in attribute_txt is a attribute list representing a sample
    combo_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//gafgyt_attacks-2//combo.csv", delimiter=',', dtype=np.str)
    junk_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//gafgyt_attacks-2//junk.csv", delimiter=',', dtype=np.str)
    scan_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//gafgyt_attacks-2//scan.csv", delimiter=',', dtype=np.str)
    tcp_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//gafgyt_attacks-2//tcp.csv", delimiter=',', dtype=np.str)
    udp_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//gafgyt_attacks-2//tcp.csv", delimiter=',', dtype=np.str)

    #print(len(attribute_csv))
    combo = list(combo_csv)
    combo = combo[1:1001]



    junk = list(junk_csv)
    junk = junk[1:1001]



    scan = list(scan_csv)
    scan = scan[1:1001]


    tcp = list(tcp_csv)
    tcp = tcp[1:1001]

    udp = list(udp_csv)
    udp = udp[1:1001]




    for i in junk:
        combo.append(i)
    for i in scan:
        combo.append(i)
    for i in tcp:
        combo.append(i)
    for i in udp:
        combo.append(i)

    attribute = np.array(combo,dtype=float)
    #attribute.astype("float32")

    label = []
    for i in range(len(attribute)):
        label.append('gafgyt')

    #label_csv = np.array(label_csv)
    label = np.array(label)
    return attribute, label


def mirai_dataset():
    # each element in attribute_txt is a attribute list representing a sample
    ack_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//mirai_attacks-2//ack.csv", delimiter=',', dtype=np.str)
    scan_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//mirai_attacks-2//scan.csv", delimiter=',', dtype=np.str)
    syn_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//mirai_attacks-2//syn.csv", delimiter=',', dtype=np.str)
    udp_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//mirai_attacks-2//udp.csv", delimiter=',', dtype=np.str)
    udpplain_csv = np.loadtxt("//Users//mengtianao//Documents//cs656//project//SimpleHome_XCS7_1002_WHT_Security_Camera//mirai_attacks-2//udpplain.csv", delimiter=',', dtype=np.str)

    #print(len(attribute_csv))
    ack = list(ack_csv)
    ack = ack[1:1001]


    scan = list(scan_csv)
    scan = scan[1:1001]


    syn = list(syn_csv)
    syn = syn[1:1001]


    udp = list(udp_csv)
    udp = udp[1:1001]


    udpplain = list(udpplain_csv)
    udpplain = udpplain[1:1001]




    for i in scan:
        ack.append(i)
    for i in syn:
        ack.append(i)
    for i in udp:
        ack.append(i)
    for i in udpplain:
        ack.append(i)

    attribute = np.array(ack,dtype=float)
    #attribute.astype("float32")

    label = []
    for i in range(len(attribute)):
        label.append('mirai')

    #label_csv = np.array(label_csv)
    label = np.array(label)

    return attribute, label

def dataset(benign_attribute, gafgyt_attribute, mirai_attribute, benign_label, gafgyt_label, mirai_label):

    benign_attribute = list(benign_attribute)
    for i in gafgyt_attribute:
        benign_attribute.append(i)

    for i in mirai_attribute:
        benign_attribute.append(i)

    attribute = benign_attribute
    attribute = np.array(attribute)

    benign_label = list(benign_label)
    for i in gafgyt_label:
        benign_label.append(i)

    for i in mirai_label:
        benign_label.append(i)

    label = benign_label
    label = np.array(label)
    return attribute, label


#devide thr original dataset to train dataset and test dataset ( 6 : 4 )
def div_train_test(attribute, label, sample_num):

    num_test = sample_num / 3

    attribute_test = []
    label_test = []
    label_act = []

    attribute_train = []
    label_train = []

    index_total = np.array(range(sample_num))
    np.random.shuffle(index_total)

    for i in range(sample_num):
        if (i < num_test):
            attribute_test.append(attribute[index_total[i]])
            label_test.append(label[index_total[i]])
            if (label[index_total[i]] == 'benign'):
                label_act.append('benign')
            else:
                label_act.append('malicious')
            continue

        attribute_train.append(attribute[index_total[i]])
        label_train.append(label[index_total[i]])

    attribute_train = np.array(attribute_train)
    label_train = np.array(label_train)
    attribute_test = np.array(attribute_test)
    label_test = np.array(label_test)
    return attribute_train, label_train, attribute_test, label_test



def Kmeans_predict(Kmeans_classfier, attribute_test):

    label_kmeans = []
    for i in attribute_test:
        predict = Kmeans_classfier.predict([i])
        #print("predict: ",predict[0])
        label_kmeans.append(predict[0])

    label_kmeans = np.array(label_kmeans)
    return label_kmeans


def DBSCAN_predict(DBSCAN_classfier):

    # label_DBSCAN = []
    # for i in attribute_test:
    #     predict = DBSCAN_classfier.predict([i])
    #     label_DBSCAN.append(predict)
    #
    # label_DBSCAN = np.array(label_DBSCAN)
    return DBSCAN_classfier.labels_
"""

def cal_error_rate(attribute_test, label_test, KNN_classfier):
    count = 0
    error_KNN = 0
    for i in attribute_test:
        predict = KNN_predict(KNN_classfier, i)
        if (predict != label_test[count]):
            error_KNN += 1
            count += 1
            continue
        count += 1

    error_rate_KNN = error_KNN / len(attribute_test)
    return error_rate_KNN

"""

def div_class(attribute_test, label_test):
    class_0 = []
    class_1 = []
    class_2 = []
    label = []
    for i in range(len(label_test)):
        if (label_test[i] == 0):
            class_0 .append(attribute_test[i])
            label.append("benign")
            continue

        if (label_test[i] == 1):
            class_1 .append(attribute_test[i])
            label.append("malicious")
            continue

        if (label_test[i] == 2):
            class_2 .append(attribute_test[i])
            label.append("malicious")
            continue

    class_0 = np.array(class_0)
    class_1 = np.array(class_1)
    class_2 = np.array(class_2)
    return class_0, class_1, class_2, label

def div_class_DBSCAN(attribute_test, label_test):
    benign = []
    class_1 = []
    class_2 = []
    count = 0

    label = []
    for i in range(len(label_test)):
        if (label_test[i] == -1):
            benign.append(attribute_test[i])
            label.append("benign")
            continue

        if (label_test[i] == 0):
            class_1 .append(attribute_test[i])
            count += 1
            label.append("malicious")
            continue

        if (label_test[i] == 1):

            class_2 .append(attribute_test[i])
            label.append("malicious")
            continue
    print("num of class 1: ", count)
    benign = np.array(benign)
    class_1 = np.array(class_1)
    class_2 = np.array(class_2)
    return benign, class_1, class_2,label


def div_class_act(attribute_test, label_test):
    class_0 = []
    class_1 = []
    class_2 = []
    label_act = []
    for i in range(len(label_test)):
        if (label_test[i] == 'benign'):
            class_0 .append(attribute_test[i])
            label_act.append('benign')
            continue

        if (label_test[i] == 'gafgyt'):
            class_1 .append(attribute_test[i])
            label_act.append("malicious")
            continue

        if (label_test[i] == 'mirai'):
            class_2 .append(attribute_test[i])
            label_act.append("malicious")
            continue

    class_0 = np.array(class_0)
    class_1 = np.array(class_1)
    class_2 = np.array(class_2)
    return class_0, class_1, class_2, label_act

def cal_error(label_act, label_classfier):

    error = 0
    for i in range(len(label_act)):
        if (label_classfier[i] != label_act[i]):
            error += 1
            continue

    return error/len(label_act)


def draw_confusion_matrix(label_act, label_classfier):
    confusion_matrix = np.array([[0, 0, 0],
                                 [0, 0, 0],
                                 [0, 0, 0]])
    for i in range(len(label_act)):
        if (label_act[i] == label_classfier[i]) and (label_act[i] == 'benign'):
            confusion_matrix[0][0] += 1

        if (label_act[i] == label_classfier[i]) and (label_act[i] == 'malicious'):
            confusion_matrix[1][1] += 1

        if (label_act[i] != label_classfier[i]) and (label_act[i] == 'benign') and (label_classfier[i] == 'malicious'):
            confusion_matrix[0][1] += 1

        if (label_act[i] != label_classfier[i]) and (label_classfier[i] == 'benign') and (label_act[i] == 'malicious'):
            confusion_matrix[1][0] += 1

    confusion_matrix[0][2] = confusion_matrix[0][0] + confusion_matrix[0][1]
    confusion_matrix[1][2] = confusion_matrix[1][0] + confusion_matrix[1][1]

    confusion_matrix[2][0] = confusion_matrix[0][0] + confusion_matrix[1][0]
    confusion_matrix[2][1] = confusion_matrix[0][1] + confusion_matrix[1][1]

    confusion_matrix[2][2] = confusion_matrix[0][2] + confusion_matrix[1][2]

    return confusion_matrix

if __name__ == "__main__":

    benign_attribute, benign_label = benign_dataset()
    gafgyt_attribute, gafgyt_label = gafgyt_dataset()
    mirai_attribute, mirai_label = mirai_dataset()
    attribute, label = dataset(benign_attribute, gafgyt_attribute, mirai_attribute, benign_label, gafgyt_label, mirai_label)
   # print(attribute[0])

    #print("num of samples: ", len(label))
    attribute_train, label_train, attribute_test, label_test = div_train_test(attribute, label, len(attribute))
    #print("num of test samples: ", len(label_test))

    #print("attribute_train: ",attribute_train)
    #data process

    #normalize the data
    normal = Normalizer().fit(attribute_train)
    normal.transform(attribute_train)
    normal.transform(attribute_test)
    #print("normal proecessed: ", attribute_test)
    print("original number of features for each sample: ", len(attribute_train[0]))
    pca = PCA(n_components = 0.98)
    processed_train_attribute = pca.fit_transform(attribute_train)
    processed_test_attribute = pca.transform(attribute_test)

    print("number of features for each sample after PCA processed: ", len(processed_train_attribute[0]))
    #print("PCA processed: ", processed_train_attribute)

    print("before normalization: ",processed_train_attribute)

    #scale the data and delete the outliers
    scaler = MinMaxScaler(feature_range=(0, 1))
    processed_train_attribute = scaler.fit_transform(processed_train_attribute)
    processed_test_attribute = scaler.fit_transform(processed_test_attribute)

    print("after normalization: ", processed_train_attribute)
    #print("scale proecessed: ", processed_train_attribute)





    # k-means method
    kmeans = KMeans(n_clusters=3, random_state=0).fit(processed_train_attribute)
    label_kmeans_test = Kmeans_predict(kmeans, processed_test_attribute)
    print(set(label_kmeans_test))

    #print("label_kmeans_test: ",label_kmeans_test)

    #DBSCAN method
    Dbscan = DBSCAN(eps = 0.0005, min_samples=80).fit(processed_test_attribute)
    label_DBSCAN_test = DBSCAN_predict(Dbscan)
    print(set(label_DBSCAN_test))
    # label_act
    class_0_kmeans, class_1_kmeans, class_2_kmeans, label_kmeans = div_class(processed_test_attribute, label_kmeans_test)
    print("kmeans test num: ", len(label_kmeans))
    #print("class_0_means: ",class_0_kmeans)
    benign_DBSCAN, class_1_DBSCAN, class_2_DBSCAN, label_DBSCAN = div_class_DBSCAN(processed_test_attribute, label_DBSCAN_test)

    benign, gafgyt, mirai, label_act = div_class_act(processed_test_attribute, label_test)

    error_kmeans = cal_error(label_act, label_kmeans)

    error_DBSCAN = cal_error(label_act, label_DBSCAN)

    print("error_kmeans_rate: ", error_kmeans)
    print("error_DBSCAN_rate: ", error_DBSCAN)
    kmeans_confusion_matrix = draw_confusion_matrix(label_act, label_kmeans)
    print("kmeans false positives: ", kmeans_confusion_matrix[0][1])
    print("kmeans true positives: ", kmeans_confusion_matrix[1][1])
    print("kmeans confusion matrix")
    print(kmeans_confusion_matrix)
    DBSCAN_confusion_matrix = draw_confusion_matrix(label_act, label_DBSCAN)
    print("DBSCAN false positives: ", DBSCAN_confusion_matrix[0][1])
    print("DBSCAN true positives: ", DBSCAN_confusion_matrix[1][1])
    print("DBSCAN confusion matrix")
    print(DBSCAN_confusion_matrix)





    # print("length of attribute: ", len(attribute[0]))
    # print("PCA len: ", len(processed_train_attribute[0]))
    # print("PCA len: ", len(processed_test_attribute[0]))
    # print("number of train: ", len(attribute_train))
    # print("number of test: ", len(attribute_test))
    # print("number of samples: ", len(attribute))
    #print(len(label))


    plt.figure(1)
    plt.title('k-means')
    predict_class0_kmeans = plt.scatter(class_0_kmeans[:,0], class_0_kmeans[:,1],c = 'r', alpha=0.6)
    predict_class1_kmeans = plt.scatter(class_1_kmeans[:,0], class_1_kmeans[:,1],c = 'b', alpha=0.6)
    predict_class2_kmeans = plt.scatter(class_2_kmeans[:, 0], class_2_kmeans[:, 1], c='b', alpha=0.6)
    plt.legend((predict_class0_kmeans, predict_class1_kmeans), ("benign", "malicious"), loc = 0)
    plt.xlim(0, 0.01)
    plt.ylim(0, 0.5)

    #print("class_1_DBSCAN: ", class_1_DBSCAN)
    plt.figure(2)
    plt.title('DBSCAN')
    predict_class0_DBSCAN = plt.scatter(benign_DBSCAN[:,0], benign_DBSCAN[:,1],c = 'r', alpha=0.6)
    predict_class1_DBSCAN = plt.scatter(class_1_DBSCAN[:,0], class_1_DBSCAN[:,1],c = 'b', alpha=0.6)
    predict_class2_DBSCAN = plt.scatter(class_2_DBSCAN[:, 0], class_2_DBSCAN[:, 1], c='b', alpha=0.6)
    plt.legend((predict_class0_DBSCAN, predict_class1_DBSCAN), ("benign", "malicious"), loc = 0)
    plt.xlim(0, 0.01)
    plt.ylim(0, 0.5)


    plt.figure(3)
    plt.title('Actual result')
    class0 = plt.scatter(benign[:,0], benign[:,1],c = 'r', alpha=0.6)
    class1 = plt.scatter(gafgyt[:,0], gafgyt[:,1],c = 'b', alpha=0.6)
    class2 = plt.scatter(mirai[:, 0], mirai[:, 1], c='b', alpha=0.6)
    plt.legend((class0, class1), ("benign", "malicious"), loc = 0)

    plt.xlim(0, 0.01)
    plt.ylim(0, 0.5)

    plt.figure(4)
    plt.title('k-means')
    predict_class0_kmeans = plt.scatter(class_0_kmeans[:,0], class_0_kmeans[:,1],c = 'r', alpha=0.6)
    predict_class1_kmeans = plt.scatter(class_1_kmeans[:,0], class_1_kmeans[:,1],c = 'b', alpha=0.6)
    predict_class2_kmeans = plt.scatter(class_2_kmeans[:, 0], class_2_kmeans[:, 1], c='b', alpha=0.6)
    plt.legend((predict_class0_kmeans, predict_class1_kmeans), ("benign", "malicious"), loc = 0)

    plt.figure(5)
    plt.title('DBSCAN')
    predict_class0_DBSCAN = plt.scatter(benign_DBSCAN[:,0], benign_DBSCAN[:,1],c = 'r', alpha=0.6)
    predict_class1_DBSCAN = plt.scatter(class_1_DBSCAN[:,0], class_1_DBSCAN[:,1],c = 'b', alpha=0.6)
    predict_class2_DBSCAN = plt.scatter(class_2_DBSCAN[:, 0], class_2_DBSCAN[:, 1], c='b', alpha=0.6)
    plt.legend((predict_class0_DBSCAN, predict_class1_DBSCAN), ("benign", "malicious"), loc = 0)

    plt.figure(6)
    plt.title('Actual result')
    class0 = plt.scatter(benign[:,0], benign[:,1],c = 'r', alpha=0.6)
    class1 = plt.scatter(gafgyt[:,0], gafgyt[:,1],c = 'b', alpha=0.6)
    class2 = plt.scatter(mirai[:, 0], mirai[:, 1], c='b', alpha=0.6)
    plt.legend((class0, class1), ("benign", "malicious"), loc = 0)
    plt.show()
