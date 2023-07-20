# phylogenetic tree implementation in python

from ctypes import sizeof
from importlib.resources import path
import os
import socket
from tkinter import font
from turtle import forward
import matplotlib.pylab
import pandas as pd
from matplotlib import pyplot as plt
from Bio import Phylo
from MyProjectApp.models import count_check
# import yes


wdir = os.getcwd()
print(wdir)
#hostname = socket.gethostname()
#local_ip = socket.gethostbyname(hostname)

#print(local_ip)
#print(type(local_ip))

import Bio

from Bio.Phylo.Consensus import bootstrap_trees, get_support

# file = input("Input your query file")
# print("file is:" + file)
# user Browse sequence
# read sequence file in fasta , .faa, .fa, format.
# file = open('GLI family Seq 2007.fasta', 'r')
# f = file.read()
# print(f)

# Multiple sequence alignment using clustalw
in_file = ""
out_file = ""
fmt = ""
outtree = ""
cls = ""
of = ""


def configuration(inFile, outFile, FMT, outTree, CLS, OF, complete_del, clustering_type):
    print("Multiple sequence alignment using clustalw")
    # in_file = "GLI family Seq 2007.fasta"
    in_file = inFile
    # out_file = "Alignment.aln"
    out_file = outFile
    # fmt = "clustal"  # its will provide "sequence.dnd" file and "genealign.aln" file
    fmt = FMT
    # matrix = "IUB"
    # outtree = "nexus"
    outtree = outTree
    # cls = "NJ"
    cls = CLS

    # of = "off"
    of = OF
    print(in_file, out_file, fmt, outtree, cls, of)
    print("Success")


def start(inFile, outFile, FMT, outTree, CLS, OF, complete_del, clustering_type):
    outtree = outTree
    from Bio.Align.Applications import ClustalwCommandline
    from matplotlib import pyplot as plt
    from Bio import AlignIO, Phylo, SeqIO

    h=count_check.objects.get(id=1).pid
    mnmn=h+1
    kkk=str(mnmn)
    h1=count_check.objects.get(id=1)
    h1.pid=mnmn
    h1.save()
    os.system("mkdir "+kkk+"")
    BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = (os.path.join(BASE_DIR1,kkk,),)
    #os.system('copy clustalw2.exe '+kkk+'')
    #clustalw_exe =kkk+"/clustalw2.exe"
    clustalw_exe ="clustalw2.exe"

    clustalw_cline = ClustalwCommandline(clustalw_exe, infile=inFile, outfile=outFile, output=FMT, gapopen=10.00,
                                         gapext=0.20, negative='off')
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
    stdout, stderr = clustalw_cline()
    # print(clustalw_cline)

    # Read alignment file using alignIO

    alignment = AlignIO.read(outFile, FMT)
    # print(align)
    for record in alignment:
        print("%s - %s" % (record.id, record.seq))
    # convert file from clustal to phylip and clustal to fasta, now user has 3 sequence file format options
    # 1: aln 2: phy 3:fasta
    AlignIO.convert("Alignment.aln", "clustal", "Alignment.phy", "phylip-relaxed")
    AlignIO.convert("Alignment.aln", "clustal", "Alignment.fasta", "fasta")

    # After MSA create distance matrix.
    # for P-distance matrix
    # from Bio import AlignIO
    # import pandas as pd
    # from scipy.spatial import distance_matrix
    from Bio import AlignIO

    # alignment = AlignIO.read("Alignment.aln", "clustal")
    # while True:

    # complete_del = input("Do you want complete deletion? 'yes' or 'no' ")

    if complete_del == "yes":

        def cut_a_gap(align):
            n = float(len(align[0]))
            i = 0
            while i < n:
                if align[:, i].count('-') / n:
                    if i == 0:
                        align = align[:, 1:]
                    elif i + 1 == n:
                        align = align[:, :i]
                    else:
                        align = align[:, :i] + align[:, i + 1:]
                    n -= 1  # seq. 1 shorter
                else:  # nothing to delete, proceed
                    i += 1
                # print(align)
                with open('col_del.aln', 'w+') as output_handle:
                    SeqIO.write(align, output_handle, "clustal")

        cut_a_gap(alignment)

        def p_dist(seq1, seq2):
            ali_len = len(seq1)
            assert ali_len == len(seq2)
            return sum(0 if nuc1 == nuc2 else 1 for (nuc1, nuc2) in zip(seq1, seq2)) / ali_len

        ali = AlignIO.read("col_del.aln", "clustal")
        nb_seq = len(ali)
        distances = {}
        for i in range(nb_seq - 1):
            rec1 = ali[i]
            j = i + 1
            while j < nb_seq:
                rec2 = ali[j]
                distances[(rec1.id, rec2.id)] = p_dist(rec1.seq, rec2.seq)
                j += 1

        print(*distances.items(), sep="\n")
        os.system("copy nul > "+kkk+"Distance.txt")
        with open(''+kkk+'/Pairwise Distance.txt', 'w+') as f:
            f.write(str(distances))
            f.close()

        # Calculate distance matrix
        print("Distance Matrix")
        from Bio.Phylo.TreeConstruction import DistanceCalculator
        from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

        # choose of model depend on user
        # for protein sequences alignment matrixes like BLOSUM62, GONNET, PAM, ID
        # For DNA seqs : 'identity', 'blastn', 'trans' / these 3 dna models are used/
        # for Protein seqs : all the remaining models.
        # we can also create distance matrix from models
        models = ['identity', 'blastn', 'trans', 'benner22', 'benner6', 'benner74', 'dayhoff', 'feng', 'genetic',
                  'gonnet1992',
                  'hoxd70', 'johnson', 'jones', 'levin', 'mclachlan', 'mdm78', 'rao', 'risler', 'schneider', 'str',
                  'blosum45', 'blosum50', 'blosum62', 'blosum80', 'blosum90', 'pam250', 'pam30', 'pam70']

        # DNA Models = 'identity', 'blastn', 'trans' Protein Models = 'benner22', 'benner6', 'benner74', 'dayhoff',
        # 'feng', 'genetic', 'gonnet1992','hoxd70', 'johnson', \ 'jones', 'levin', 'mclachlan', 'mdm78', 'rao', 'risler',
        # 'schneider', 'str','blosum45', 'blosum50',\ 'blosum62', 'blosum80', 'blosum90', 'pam250', 'pam30', 'pam70'

        # identity matrix give results based on P-distance.
        calculator = DistanceCalculator('identity')
        dm = calculator.get_distance(ali)
        # print(dm)
        os.system("copy nul > "+kkk+"Distance Matrix.csv")
        with open(''+kkk+'/Distance Matrix.csv', 'w+') as f:
            f.write(str(dm))
            f.close()
        
        def change_format(path, name):
            file_name=path
            print(os.listdir(file_name))

            file = open(file_name+"/"+name)
            lines=file.readlines()
            new_file=open(file_name+"/Distance Matrix.csv","w")
            for l in lines:
                print(l)
                new_file.write(l.replace("\t",","))
            file.close()
            new_file.close()
        change_format(kkk,"Distance Matrix.csv")



            
        print("Phylogenetic tree")
        # Phylogenetic tree with bootstrap values???
        constructor = DistanceTreeConstructor(calculator)
        # clustering_type = input("Select tree clustering type? 'nj' or 'upgma' ")
        if clustering_type == "nj":
            tree = constructor.nj(dm)
        else:
            tree = constructor.upgma(dm)
        tree.rooted = True
        print(tree)

        with open('Tree.txt', 'w+') as f:
            f.write(str(tree))
            f.close()
            Bio.Phylo.write(tree, outtree,
                            "newick")  # this line provide tree file in newick format. on the bass of newick
        # file next phylogeny test is coded.

        # after construction of phylogenetic tree ,apply phylogeny test like bootstrap test. but how to add bootstrap
        # values?
        trees = bootstrap_trees(ali, 100, constructor)
        tree = list(Phylo.parse("nexus", "newick"))
        target_tree = tree[0]
        tree = list(trees)
        for node in target_tree.get_nonterminals():
            node.name = None
        support_tree = get_support(target_tree, tree)
        from Bio import Phylo
        import pylab

        def get_label(leaf):
            return leaf.name

        # user can download/export tree files in phyloxml, nexus, newick formate
        print("tree generate")
        Phylo.write(support_tree, "Tree.xml", "phyloxml")
        Phylo.write(support_tree, "Tree.nex", "nexus")
        Phylo.write(support_tree, "Tree.nwk", "newick")

        # f = r"C:\Users\Azhar Sohail\PycharmProjects\pythonProject2\nexus"
        f = "Tree.nwk"
        tree = Phylo.read(f, 'newick')
        tree.ladderize()
        Phylo.draw(support_tree, label_func=get_label, do_show=False)
        pylab.axis('off')

        # user can download tree image in PDF, PNG, SVG format.
        #pylab.savefig('Tree.jpg', format='jpg', bbox_inches='tight', dpi=300)  # uncommen5
        #pylab.savefig('Tree.pdf', format='pdf', bbox_inches='tight', dpi=300)  # uncommen5
        #pylab.savefig('Tree.png', format='png', bbox_inches='tight', dpi=300)  # uncommen5

        print("tree files saved")

        def plot_tree(support_tree, output_file):
            # set the size of the figure
            # fig = plt.figure(figsize=(10, 10), dpi=60)
            # fig.set_size_inches(10, 20) # in inches
            # plt.rcParams.update({'font.size': 10})
            # axes = fig.add_subplot(1, 1, 1)
            Phylo.draw_ascii(support_tree)
            fig1 = plt.gcf()
            tree.ladderize()
            # Phylo.draw(support_tree, label_func=get_label, axes=axes)
            # Phylo.draw(support_tree, branch_labels=None, show_confidence=True, label_func=get_label)
            pylab.axis('off')
            plt.tight_layout()
            fig = matplotlib.pylab.gcf()
            fig.set_size_inches(18.5, 10.5, forward=True)
            plt.savefig('Tree.png', format='png', bbox_inches='tight', dpi=300)
            plt.savefig('Tree.pdf', format='pdf', bbox_inches='tight', dpi=300)
            #plt.savefig('Tree.jpg', format='jpg', bbox_inches='tight', dpi=300)
            #Phylo.draw_graphviz(support_tree)
            #Phylo.draw(support_tree, branch_labels=None, show_confidence=True, label_func=get_label)
            #pylab.show()
            fig1.savefig(output_file, dpi=300, bbox_inches='tight', transparent=True)
            return

        plot_tree(support_tree, "Tree.pdf")  # uncomment

    else:
        def p_dist(seq1, seq2):
            ali_len = len(seq1)
            assert ali_len == len(seq2)
            return sum(0 if nuc1 == nuc2 else 1 for (nuc1, nuc2) in zip(seq1, seq2)) / ali_len

        ali = AlignIO.read("Alignment.aln", "clustal")
        nb_seq = len(ali)
        distances = {}
        for i in range(nb_seq - 1):
            rec1 = ali[i]
            j = i + 1
            while j < nb_seq:
                rec2 = ali[j]
                distances[(rec1.id, rec2.id)] = p_dist(rec1.seq, rec2.seq)
                j += 1

        print(*distances.items(), sep="\n")
        
        os.system("copy nul > "+kkk+"Pairwise Distance.txt")
        with open(''+kkk+'/Pairwise Distance.txt', 'w+') as f:
            f.write(str(distances))
            f.close()

        # Calculate distance matrix
        print("Distance Matrix")
        from Bio.Phylo.TreeConstruction import DistanceCalculator
        from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

        # choose of model depend on user
        # for protein sequences alignment matrices like BLOSUM62, GONNET, PAM, ID
        # For DNA seqs : 'identity', 'blastn', 'trans' / these 3 dna models are used/
        # for Protein seqs : all the remaining models.
        # we can also create distance matrix from models
        models = ['identity', 'blastn', 'trans', 'benner22', 'benner6', 'benner74', 'dayhoff', 'feng', 'genetic',
                  'gonnet1992',
                  'hoxd70', 'johnson', 'jones', 'levin', 'mclachlan', 'mdm78', 'rao', 'risler', 'schneider', 'str',
                  'blosum45', 'blosum50', 'blosum62', 'blosum80', 'blosum90', 'pam250', 'pam30', 'pam70']

        # DNA Models = 'identity', 'blastn', 'trans' Protein Models = 'benner22', 'benner6', 'benner74', 'dayhoff',
        # 'feng', 'genetic', 'gonnet1992','hoxd70', 'johnson', \ 'jones', 'levin', 'mclachlan', 'mdm78', 'rao', 'risler',
        # 'schneider', 'str','blosum45', 'blosum50',\ 'blosum62', 'blosum80', 'blosum90', 'pam250', 'pam30', 'pam70'

        # identity matrix give results based on P-distance.
        calculator = DistanceCalculator('identity')
        dm = calculator.get_distance(alignment)
        print(dm)
        os.system("copy nul > "+kkk+"Distance Matrix.csv")
        with open(''+kkk+'/Distance Matrix.csv', 'w+') as f:
            f.write(str(dm))
            f.close()

        def change_format(path, name):
            file_name=path
            print(os.listdir(file_name))

            file = open(file_name+"/"+name)
            lines=file.readlines()
            new_file=open(file_name+"/Distance Matrix.csv","w")
            for l in lines:
                print(l)
                new_file.write(l.replace("\t",","))
            file.close()
            new_file.close()
        change_format(kkk,"Distance Matrix.csv")        
        
        print("Phylogenetic tree")
        # Phylogenetic tree with bootstrap values???
        constructor = DistanceTreeConstructor(calculator)
        # clustering_type = input("Select tree clustering type? 'nj' or 'upgma' ")
        if clustering_type == "nj":
            tree = constructor.nj(dm)
            tree.rooted = True
        else:
            tree = constructor.upgma(dm)
            tree.rooted = True
        print(tree)
        
        with open('Tree.txt', 'w+') as f:
            f.write(str(tree))
            f.close()
            Bio.Phylo.write(tree, outtree,"newick")  # this line provide tree file in nexus format. on the bass of nexus
        # file next phylogeny test is coded.

        # after construction of phylogenetic tree ,apply phylogeny test like bootstrap test. but how to add bootstrap
        # values?
        trees = bootstrap_trees(alignment, 100, constructor)
        tree = list(Phylo.parse("nexus", "newick"))
        target_tree = tree[0]
        tree = list(trees)

        for node in target_tree.get_nonterminals():
            node.name = None
        support_tree = get_support(target_tree, tree)
        from Bio import Phylo
        import pylab

        def get_label(leaf):
            return leaf.name

        # user can download/export tree files in phyloxml, nexus, newick formate
       # path = 'C:/Users/Azhar Sohail/PycharmProjects/RamshaProject/myproject/MyProjectApp/static/images'
        Phylo.write(support_tree, "Tree.xml", "phyloxml")
        Phylo.write(support_tree, "Tree.nex", "nexus")
        Phylo.write(support_tree, "Tree.nwk", "newick")
        
        #f = r"C:\Users\Azhar Sohail\PycharmProjects\pythonProject2\nexus"
        f = "Tree.nwk"
        tree = Phylo.read(f, 'newick')
        tree.ladderize()
        Phylo.draw(support_tree, label_func=get_label, do_show=False)
        pylab.axis('off')
        
        # user can download tree image in PDF, PNG, SVG format.
        #pylab.savefig('Tree.jpg', format='jpg', bbox_inches='tight', dpi=300)  # uncomment
        #pylab.savefig('Tree.pdf', format='pdf', bbox_inches='tight', dpi=300)  # uncomment
        #pylab.savefig('Tree.png', format='png', bbox_inches='tight', dpi=300)  # uncomment

        def plot_tree(support_tree, output_file):
              # set the size of the figure
            # fig = plt.figure(figsize=(10, 10), dpi=60)
            # fig.set_size_inches(10, 20) # in inches
            # plt.rcParams.update({'font.size': 10})
            # axes = fig.add_subplot(1, 1, 1)
            Phylo.draw_ascii(support_tree)
            fig1 = plt.gcf()
            tree.ladderize()
            # Phylo.draw(support_tree, label_func=get_label, axes=axes)
            # Phylo.draw(support_tree, branch_labels=None, show_confidence=True, label_func=get_label)
            pylab.axis('off')
            plt.tight_layout()
            fig = matplotlib.pylab.gcf()
            fig.set_size_inches(18.5, 10.5, forward=True)
            plt.savefig('Tree.png', format='png', bbox_inches='tight', dpi=300)
            plt.savefig('Tree.pdf', format='pdf', bbox_inches='tight', dpi=300)
            #plt.savefig('Tree.jpg', format='jpg', bbox_inches='tight', dpi=300)
            #Phylo.draw_graphviz(support_tree)
            #Phylo.draw(support_tree, branch_labels=None, show_confidence=True, label_func=get_label)
            #pylab.show()
            fig1.savefig(output_file, dpi=300, bbox_inches='tight', transparent=True)
            return

        plot_tree(support_tree, "Tree.pdf")  # uncomment
    path = 'C:/Users/Azhar Sohail/PycharmProjects/Project/myproject/MyProjectApp/static/images'
    pylab.savefig(os.path.join(path, 'PhyTree.png'), format='png', bbox_inches='tight', dpi=300)
        
                    # tree file formate: Newick, phyloXML, Nexus, phylip
    try:
        os.system("copy Alignment.aln "+kkk+"")
        os.system("del Alignment.aln")
    except:
        pass
    try:
        os.system("copy Alignment.fasta "+kkk+"")
        os.system("del Alignment.fasta")
    except:
        pass
    try:
        os.system("copy Alignment.phy "+kkk+"")
        os.system("del Alignment.phy")
    except:
        pass
    try:
        os.system("copy Tree.xml "+kkk+"")
        os.system("del Tree.xml")
    except:
        pass
    try:
        os.system("copy Tree.nwk "+kkk+"")
        os.system("del Tree.nwk")
    except:
        pass
    try:
        os.system("copy Tree.nex "+kkk+"")
        os.system("del Tree.nex")
    except:
        pass
    try:
        os.system("copy Tree.pdf "+kkk+"")
        os.system("del Tree.pdf")
    except:
        pass
    
    try:
        os.system("copy Tree.png "+kkk+"")
        os.system("del Tree.png")
    except:
        pass
    try:
        os.system("copy nexus "+kkk+"")
        os.system("del nexus")
    except:
        pass
    
    try:
        os.system("copy Tree.txt "+kkk+"")
        os.system("del Tree.txt")
    except:
        pass
    return mnmn
    