import numpy as np

#fonction d'activation
def sigmoid(z):
    return 1/(1+np.exp(-z))


#fonction d'initialisation
def initialize(_nx, _nh, _ny):
    W1 = np.random.randn(_nh, _nx)
    b1 = np.zeros((_nx, 1))
    W2 = np.random.randn(_ny, _nh)
    b2 = np.zeros((_ny, 1))
    
    params = {
        "W1":W1,
        "b1":b1,
        "W2":W2,
        "b2":b2
    }
    return params

#fonction de propagation
def avnt_propagation(X, params):
    W1 = params["W1"]
    b1 = params["b1"]
    W2 = params["W2"]
    b2 = params["b2"]
    
    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    
    cache = {
        "Z1":Z1,
        "A1":A1,
        "Z2":Z2,
        "A2":A2
    }
    return A2, cache

#fonction de cout
def cout(A2, Y):
    m = Y.shape[1]
    proba = np.multiply(np.log(A2), Y) + np.multiply(np.log(1-A2), 1-Y)
    cout = - np.sum(proba)/m
    return cout

#fonction de retropropagation
def backward_propagation(params, cache, X, Y):
    m = X.shape[1]
    W2 = params["W2"]
    
    A1 = cache["A1"]
    A2 = cache["A2"]
    
    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T)/m
    db2 = np.sum(dZ2, axis=1, keepdims=True)/m
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1-np.power(A1, 2))
    dW1 = np.dot(dZ1, X.T)/m
    db1 = np.sum(dZ1, axis=1, keepdims=True)/m
    
    grads = {
        "dW1":dW1,
        "db1":db1,
        "dW2":dW2,
        "db2":db2
    }
    return grads

#fonction d'entrainement
def train(X, Y, _nx, nh, ny, iter):
    params = initialize(_nx, nh, ny)
    for i in range(iter):
        A2, cache = avnt_propagation(X, params)
        cout1 = cout(A2, Y)
        grads = backward_propagation(params, cache, X, Y)
        params = update_params(params, grads)
        if i % 100 == 0:
            print("Cout apres iteration %i: %f" %(i, cout1))
    return params

#fonction de mise a jour des parametres
def update_params(params, grads):
    W1 = params["W1"] - grads["dW1"]
    b1 = params["b1"] - grads["db1"]
    W2 = params["W2"] - grads["dW2"]
    b2 = params["b2"] - grads["db2"]
    
    params = {
        "W1":W1,
        "b1":b1,
        "W2":W2,
        "b2":b2
    }
    return params

#fonction de prediction
def predict(params, X):
    A2, cache = avnt_propagation(X, params)
    Y_prediction = np.zeros((1, X.shape[1]))
    for i in range(A2.shape[1]):
        if A2[0, i] > 0.5:
            Y_prediction[0, i] = 1
        else:
            Y_prediction[0, i] = 0
    return Y_prediction

#fonction de precision
def precision(Y_prediction, Y):
    
    m = Y.shape[1]
    precision = np.sum((Y_prediction == Y)/m)
    return str(precision*100) + "%"

#resultat du modele
def result(Y_prediction, Y):
    print("Prediction: " + str(Y_prediction))
    print("Precision: " + str(precision(Y_prediction, Y)))


#test du modele en demandant a l'utilisateur de saisir les donnees entre 1 ou 0, autre que 1 ou 0 le programme continue de demander a l'utilisateur de saisir les donnees en 1 ou 0

#demander a et b a l'utilisateur
while True:
    try:
        a = int(input("Saisir a: "))
        if a == 1 or a == 0:
            break
        else:
            print("Saisir 1 ou 0")
    except ValueError:
        print("Saisir 1 ou 0")
    except NameError:
        print("Saisir 1 ou 0")
    except SyntaxError:
        print("Saisir 1 ou 0")
    except TypeError:
        print("Saisir 1 ou 0")
    except AttributeError:
        print("Saisir 1 ou 0")
    
while True:
    try:
        b = int(input("Saisir b: "))
        if b == 1 or b == 0:
            break
        else:
            print("Saisir 1 ou 0")
    except ValueError:
        print("Saisir 1 ou 0")
    except NameError:
        print("Saisir 1 ou 0")
    except SyntaxError:
        print("Saisir 1 ou 0")
    except TypeError:
        print("Saisir 1 ou 0")
    except AttributeError:
        print("Saisir 1 ou 0")
   


X = np.array([[a], [b]])
Y = np.array([[a^b]]) #xor


params = train(X, Y, 2, 2, 1, 1000) #entrainement du modele avec 1000 iterations
Y_prediction = predict(params, X)
result(Y_prediction, Y)