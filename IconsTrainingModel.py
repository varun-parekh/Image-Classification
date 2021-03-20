class IconTrainingModel:

    def create_dataset(img_folder):
        img_data_array=[]
        class_name=[]
        for dir1 in os.listdir(img_folder):
            for file in os.listdir(os.path.join(img_folder, dir1)):
                #print("file",file)
                image_path= os.path.join(img_folder, dir1,  file)
                #print("image_path",image_path)
                image= imread( image_path)#, cv2.COLOR_BGR2RGB)
                #if(isempty(image))
                image=cv2.resize(image,(img_height, img_width),interpolation = cv2.INTER_AREA)
                image=np.array(image)
                image = image.astype('float32')
                image /= 255
                img_data_array.append(image)
                class_name.append(dir1)
        img=np.array(img_data_array)
        msk=np.array(class_name)
        return img_data_array, class_name

    def target_val(y_train):
        target_dict={k: v for v, k in enumerate(np.unique(y_train))}
        target_dict
        target_val=  [target_dict[y_train[i]] for i in range(len(y_train))]
        print(target_val)
        return target_val
    
    def cnn_model(num_classes):
        model = Sequential([
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
        ])
        return model

    def train_model(model, epoch, x_train, target_val, batch_size, verbose):
        model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
        history = model.fit(x_train,np.array(target_val), batch_size=10, epochs=5, verbose=1)
        return history
       
