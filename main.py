# Read config
import argparse
import setting
import json

# Run model
from net import run_network

# Logging
from utils import logger

# for debug
import pdb

def main():
    # Read argument
    parser = argparse.ArgumentParser()
    """
    Explanation for arguments

    # device options
    parser.add_argument('--cuda', action = 'store_true', help = 'using GPU?')
    
    # training options
    parser.add_argument('--seed', type = int, default = 42, help = 'random seed')
    parser.add_argument('--epochs', type = int, default = 200, help = 'num of train epochs')
    parser.add_argument('--lr', type = float, default = 0.01, help = 'initial learning rate')
    parser.add_argument('--loss_ft', type = str, default = "nll", help = 'loss function. nll / cross-entropy')
    parser.add_argument('--weight_decay',type = float, default = 5e-4, help = 'weight decay')
    parser.add_argument('--dim_hidden', type = int, default = 16, help = 'dim of hidden layers')
    parser.add_argument('--n_hidden_layer', type = int, default = 2, help = 'num of hidden layers')
    parser.add_argument('--batch_size', type = int, default = 1)
    parser.add_argument('--bias', action = 'store_true', help = 'whether to use bias')
    # Select Data
    parser.add_argument('--data', type = str, default = 'Planetoid', help = 'dataset to use')
    #parser.add_argument('--data_name', type = str, default = 'Cora', help = 'which data to use?')

    # Model to Use
    parser.add_argument('--model', type = str, default = 'GCN', help = 'GraphML model to use')

    # Run whole process? or train/val/test seperate?
    parser.add_argument('--process', type = str, default = 'whole', help = 'train save only trained model. test run the saved model')

    #Additional Option
    parser.add_argument('--use_package_implementation', action = 'store_true', help = 'Using Implementation from package or own implementation?')
    """
    args = parser.parse_args([])

    # Read config written by json file
    with open('config.json', 'r') as f:
        config = json.load(f)
    for key, item in config['DEFAULT'].items():
        setattr(args, key, item)
    
    #Setting the Logger
    Logger = logger.Logger()
    Logger.add_level("TRAIN", 11)
    Logger.add_level("VAL", 12)
    Logger.add_level("TEST", 13)
    with open('logging.json', 'rt') as f:
        Logger.read_json(json.load(f), args.logger_option)

    # part where actually run the network
    run_network(args, Logger)

if __name__ == '__main__':
    main()