import csv, numpy as np

## Formal ETL:

# Extracting data out of the given zipped files:
csv_train = open('training.csv','rb')
train_csv = csv.reader(csv_train)

csv_test = open('test.csv','rb')
test_csv = csv.reader(csv_test)
print "Extraction is done!";

# Transforming extracted data:
testID = [];
testData = [];
trainData = [];
trainLabel = [];
LabelName = [];

test_counter = 0;
train_counter = 0;

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        pass
    return False

for row in test_csv:
    if (test_counter != 0):
        col_counter = 0;
        for col in row:
            if (col_counter == 0):
                col = str(col);
                testID.append(float(col));
            else:
                col = str(col);
                rowData = col.split(' ');
                rowData = map(lambda x: float(x), rowData);
                testData.append(np.array(rowData));
            col_counter += 1;
    test_counter += 1;

for row in train_csv:
    if (train_counter == 0):
        col_counter = 0;
        for col in row:
            if (col_counter < 30):
                LabelName.append(col);
            else:
                break;
            col_counter += 1;
    if (train_counter != 0):
        col_counter = 0;
        rowLabel = [-1 for x in range(30)];
        for col in row:
            if (col_counter == 30):
                col = str(col);
                rowData = col.split(' ');
                rowData = map(lambda x: float(x), rowData);
                trainData.append(np.array(rowData));
            else:
                col = str(col);
                if (is_float(col)):
                    rowLabel[col_counter] = float(col);
            col_counter += 1;
        trainLabel.append(np.array(rowLabel));
    train_counter += 1;

testData = np.array(testData);
testID = np.array(testID);
trainData = np.array(trainData);
trainLabel = np.array(trainLabel);
LabelName = np.array(LabelName);
print "Transformation is done!";

# Storing transformed data into the easily readable files:
np.savetxt('trainLabel.csv',trainLabel,delimiter=',');
np.savetxt('trainData.csv',trainData,delimiter=',');
np.savetxt('LabelName.csv',LabelName,delimiter=',',fmt='%s');
np.savetxt('testData.csv',testData,delimiter=',');
np.savetxt('testID.csv',testID,delimiter=',');
print "Storing is done!";