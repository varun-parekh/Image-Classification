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

    def target_val(y_train)
    target_dict={k: v for v, k in enumerate(np.unique(y_train))}
    target_dict
    target_val=  [target_dict[y_train[i]] for i in range(len(y_train))]
    print(target_val)
    return target_val

    def help(self):
        return ('Hey There!!')
