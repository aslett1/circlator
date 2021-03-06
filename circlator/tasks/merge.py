import argparse
import circlator

def run():
    parser = argparse.ArgumentParser(
        description = 'Merge original and new assembly',
        usage = 'circlator merge [options] <original.fasta> <new.fasta> <outprefix>'
    )

    parser.add_argument('--diagdiff', type=int, help='Nucmer diagdiff option [%(default)s]', metavar='INT', default=25)
    parser.add_argument('--min_id', type=float, help='Nucmer minimum percent identity [%(default)s]', metavar='FLOAT', default=95)
    parser.add_argument('--min_length', type=int, help='Minimum length of hit for nucmer to report [%(default)s]', metavar='INT', default=500)
    parser.add_argument('--min_length_merge', type=int, help='Minimum length of nucmer hit to use when merging [%(default)s]', metavar='INT', default=4000)
    parser.add_argument('--breaklen', type=int, help='breaklen option used by nucmer [%(default)s]', metavar='INT', default=500)
    parser.add_argument('--min_spades_circ_pc', type=float, help='Min percent of contigs needed to be covered by nucmer hits to spades circular contigs [%(default)s]', metavar='FLOAT', default=95)
    parser.add_argument('--ref_end', type=int, help='max distance allowed between nucmer hit and end of input assembly contig [%(default)s]', metavar='INT', default=15000)
    parser.add_argument('--reassemble_end', type=int, help='max distance allowed between nucmer hit and end of reassembly contig [%(default)s]', metavar='INT', default=1000)
    parser.add_argument('--threads', type=int, help='Number of threads for remapping/assembly (only applies if --reads is used) [%(default)s]', default=1, metavar='INT')
    parser.add_argument('--reads', help='FASTA file of corrected reads that made the new assembly. Using this triggers iterative contig pair merging', metavar='FILENAME')
    parser.add_argument('--verbose', action='store_true', help='Be verbose')
    parser.add_argument('original_assembly', help='Name of original assembly', metavar='original.fasta')
    parser.add_argument('new_assembly', help='Name of new assembly', metavar='new.fasta')
    parser.add_argument('outprefix', help='Prefix of output files')
    options = parser.parse_args()

    m = circlator.merge.Merger(
        options.original_assembly,
        options.new_assembly,
        options.outprefix,
        nucmer_diagdiff=options.diagdiff,
        nucmer_min_id=options.min_id,
        nucmer_min_length=options.min_length,
        nucmer_min_length_for_merges=options.min_length_merge,
        nucmer_breaklen=options.breaklen,
        min_spades_circular_percent=options.min_spades_circ_pc,
        ref_end_tolerance=options.ref_end,
        qry_end_tolerance=options.reassemble_end,
        threads=options.threads,
        verbose=options.verbose,
        reads=options.reads,
    )
    m.run()

