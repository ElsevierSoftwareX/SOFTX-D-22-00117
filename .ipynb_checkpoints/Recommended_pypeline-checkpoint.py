import numpy as np 
                    import pandas as pd
                    from sklearn.metrics import classification_report
                    from sklearn.model_selection import train_test_split
                    from sklearn.tree import DecisionTreeClassifier

                # NOTE: Make sure that the target column is labeled 'class' in the data file
                data = pd.read_csv(dataset_path)

                X = data.drop('class', axis=1)
                y = data['class']

                X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=42)


                model= DecisionTreeClassifier(max_features=0.10236766117329577, min_samples_leaf=8,
                       min_samples_split=4)
                model.fit(X_train, Y_train)

                Y_pred = model.predict(X_test)
                score = model.score(X_test, Y_test)

                print(classification_report(Y_test, Y_pred))
                print(' Pipeline test accuracy:  %.3f' % score)

                 