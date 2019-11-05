import tensorflow.keras.backend as K

def triplet_loss(y_true, y_pred, alpha = 0.4):
    """
    Triplet loss implementation. loss = max(sum(square(anchor - positive)) - sum(square(anchor - negative)) + alpha, 0).
    The idea is to minimize distance to between anchor and positive example, while expanding distance between anchor and 
    negative example at least alpha units.
    :param y_true: true labels, dummy in this function
    :param y_pred: python list of anchor, positive, and negative feature embeddings
    :return loss: loss that will be backpropagated by the network
    """
    
    total_lenght = y_pred.shape.as_list()[-1]
#     print('total_lenght=',  total_lenght)
#     total_lenght =12
    
    anchor = y_pred[:,0:int(total_lenght*1/3)]
    positive = y_pred[:,int(total_lenght*1/3):int(total_lenght*2/3)]
    negative = y_pred[:,int(total_lenght*2/3):int(total_lenght*3/3)]

    # distance between the anchor and the positive
    pos_dist = K.sum(K.square(anchor-positive),axis=1)

    # distance between the anchor and the negative
    neg_dist = K.sum(K.square(anchor-negative),axis=1)

    # compute loss
    basic_loss = pos_dist-neg_dist+alpha
    loss = K.maximum(basic_loss,0.0)
 
    return loss
