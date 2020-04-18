from Spanish_Utils.randomize import choice
from Spanish_Utils.vocab_sets import *

#preposiciones: after, through, before, while, without
preps = ['antes de','después de','a través de', 'mientras', 'sin']
#could_should = ['podría','podrían','debería','deberían']

#all_animate_pl_nouns_f, ...
#d_fem_pl, ...
#all_p3is_anim_subj_allowing_verbs

#FOR QUIEN --> all_anim_anim_verbs_3is(p)_pst

        # What did      John read  before filing the book?
        # que  leyo juan antes de ?? el libro?
        # que_quien[0] vbpastpret_anim_to_inanim preps vb_tr det noun
        # Wh   Aux_mat  Subj V_mat ADV    V_emb  Obj
        # What did      John read  the book before filing?
        # Wh   Aux_mat  Subj V_mat Obj      ADV    V_emb


def sample(max_iter):
    for i in range(max_iter):
        prep = choice(preps)
        V2 = choice(all_non_finite_transitive_verbs)
        #quien, needs non-anim to anim verb
        if np.random.choice([True,False]):
            #plural agent and anim anim verb
            q = que_quien[1]
            V1 = choice(all_anim_anim_verbs_3ip_pst)
            #choose masc/fem agent
            if np.random.choice([True, False]):
                #fem pl
                ag_det = choice(d_fem_pl)
                ag = choice(n_fem_pl)
            else:
                #masc pl
                ag_det = choice(d_masc_pl)
                ag = choice(n_masc_pl)
        elif np.random.choice([True,False]):
            #singular agent anim anim verb
            q = que_quien[1]
            V1 = choice(all_anim_anim_verbs_3is_pst)
            if np.random.choice([True,False]):
                #fem sg
                ag_det = choice(d_fem_sg)
                ag = choice(n_fem_sg)
            else:
                #masc sg
                ag_det = choice(d_masc_sg)
                ag = choice(n_masc_sg)
        elif np.random.choice([True,False]):
            #plural agent non anim verb
            q = que_quien[0]
            V1 = choice(past_pret_3p)
            #choose masc/fem agent
            if np.random.choice([True, False]):
                #fem pl
                ag_det = choice(d_fem_pl)
                ag = choice(n_fem_pl)
            else:
                #masc pl
                ag_det = choice(d_masc_pl)
                ag = choice(n_masc_pl)
        else:
            #sg agent non anim verb
            q = que_quien[0]
            V1 = choice(past_pret_3s)
            #choose masc/fem agent
            if np.random.choice([True, False]):
                #fem pl
                ag_det = choice(d_fem_sg)
                ag = choice(n_fem_sg)
            else:
                #masc pl
                ag_det = choice(d_masc_sg)
                ag = choice(n_masc_sg)
        #make pl/sg choice for obj
        if np.random.choice([True,False]):
            #plural object
            if np.random.choice([True,False]):
                #fem pl
                obj_det = choice(d_fem_pl)
                obj = (n_fem_pl)
            else:
                #masc pl
                obj_det = choice(d_masc_pl)
                obj = choice(n_masc_pl)
        else:
            #singular objeCT
            if np.random.choice([True,False]):
                #fem sg
                obj_det = choice(d_fem_sg)
                obj = (n_fem_sg)
            else:
                #masc sg
                obj_det = choice(d_masc_sg)
                obj = choice(n_masc_sg)
    print(q,V1,ag_det,ag,prep,V2,obj_det,obj)

sample(1)
