import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


dataset_dir = '/mnt/work/datasets/'
pretrained_weights_dir = '/mnt/work/datasets/Model/'

training_models_dir = './trained_models/'
tensorbaord_dir = './tb/'

dataset_name = 'dogs'
model = 'densenet161'


batch_size = 32
learning_rate = 0.1
end_learning_rate = 0
max_iter = 20000
logging_threshold = 100
test_iteration = logging_threshold * 10
caffe_iter_size = 12
suffix = '_train_test'

model_args = [dataset_name ,model ,'lr'+str(learning_rate),'B'+str(batch_size),suffix]
model_filename = '_'.join(model_args )
model_save_path = training_models_dir+model_filename
model_save_name = "patch_model.ckpt"
tensorbaord_file = os.path.basename(os.path.normpath(model_save_path)) #'20180304-180936'


if model == 'densenet161':
    network_name = 'nets.densenet161.DenseNet161'
    imagenet__weights_filepath = pretrained_weights_dir+'tf-densenet161/tf-densenet161.ckpt'
    preprocessing_module = 'data_sampling.augmentation.densenet_preprocessing'
    preprocess_func = 'densenet'
elif model == 'resnet50':
    network_name = 'nets.resnet_v2.ResNet50'
    imagenet__weights_filepath = pretrained_weights_dir + 'resnet_v2_50/resnet_v2_50.ckpt'
    preprocess_func = 'inception_v1'
    preprocessing_module = 'data_sampling.augmentation.inception_preprocessing'


if dataset_name == 'cars':
    num_classes = 196
    db_path = dataset_dir+'stanford_cars'
    db_tuple_loader = 'data.cars_tuple_loader.CarsTupleLoader'
    train_csv_file = '/lists/train_all_sub_list.csv'
    val_csv_file = '/lists/val_all_sub_list.csv'
    test_csv_file = '/lists/test_all_sub_list.csv'
elif dataset_name == 'flowers':
    num_classes = 102
    db_path = dataset_dir+'flower102'
    db_tuple_loader = 'data.flower_tuple_loader.FLower102TupleLower'
    train_csv_file = '/lists/train_all_sub_list.csv'
    val_csv_file = '/lists/val_all_sub_list.csv'
    test_csv_file = '/lists/test_all_sub_list.csv'
elif dataset_name == 'dogs':
    num_classes = 120
    db_path = dataset_dir + 'Stanford_dogs'
    db_tuple_loader = 'data.dogs_tuple_loader.DogsTupleLoader'
    default_image_size = 224
    train_csv_file = '/lists/train_all_sub_list.csv'
    val_csv_file = '/lists/val_sub_list.csv'
    test_csv_file = '/lists/test_all_sub_list.csv'
elif dataset_name == 'birds':
    num_classes = 555
    db_path = dataset_dir+'nabirds'
    db_tuple_loader = 'data.birds_tuple_loader.BirdsTupleLoader'
    default_image_size = 224
    train_csv_file = '/lists/train_all_sub_list.csv'
    val_csv_file = '/lists/val_sub_list.csv'
    test_csv_file = '/lists/test_all_sub_list.csv'
elif dataset_name == 'aircrafts':
    num_classes = 100
    db_path = dataset_dir+'aircrafts'
    db_tuple_loader = 'data.aircrafts_tuple_loader.AircraftsTupleLoader'
    train_csv_file = '/lists/train_all_sub_list.csv'
    val_csv_file = '/lists/val_all_sub_list.csv'
    test_csv_file = '/lists/test_all_sub_list.csv'
elif dataset_name == 'cub':
    num_classes = 200
    db_path = dataset_dir+'CUB_200_2011'
    db_tuple_loader = 'data.CUB_tuple_loader.CUBTupleLoader'
    train_csv_file = '/lists/train_all_sub_list.csv'
    val_csv_file = '/lists/val_sub_list.csv'
    test_csv_file = '/lists/test_all_sub_list.csv'

def touch_dir(path):
    if(not os.path.exists(path)):
        os.makedirs(path)

touch_dir(model_save_path)
