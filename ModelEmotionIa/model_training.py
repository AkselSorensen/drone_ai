from tensorflow.keras.models import load_model

def train_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
    # Sauvegarder le modèle entraîné
    model.save('emotion_model.h5')
