from commonvar import *

def genfig(result_df, prop_df_dict, figname, score_type, valsplit, method_lst, network):
	fig, axes = plt.subplots(1, 3, figsize=(8,4))

	for prop_idx, prop in enumerate(prop_lst):
		axes[prop_idx].set_xlabel(prop)
		if prop_idx == 0:
			axes[prop_idx].set_ylabel('log2(auPRC/prior)')
		if prop_idx == 2:
			axes[prop_idx].set_xlim([0,0.06])
		# if prop_idx == 0:
		# 	axes[prop_idx].set_title(method, fontsize=18)
		# # if method_idx == 0:
		# 	ax.set_ylabel(score_type)
		# else:
		# 	ax.set_ylabel('')
		# if prop != 'Number of Genes':
		# 	axes[prop_idx].set_xscale('log')

		for color, sub_gsc_lst in gsc_color_dict.items():
			combined_prop_ary = np.array([])
			combined_score_ary = np.array([])
			for gsc in sub_gsc_lst:
				indicator = helperfun.subset_indicator(result_df, network=network, gsc=gsc, \
									method='SL-A', score_type=score_type, valsplit=valsplit)
				sub_df = result_df[indicator]
				score_ary, prop_ary = helperfun.get_score_prop_ary(prop_df_dict, prop, sub_df, network, gsc)
				combined_prop_ary = np.append(combined_prop_ary, prop_ary)
				combined_score_ary = np.append(combined_score_ary, score_ary)
			if prop_idx == 0:
				bins_ = [10,20,30,40,50,100,150,200,300,400,500]
			else:
				bins_ = 10
			sns.regplot(combined_prop_ary, combined_score_ary, color=color, x_bins=bins_, \
						fit_reg=False, ax=axes[prop_idx], scatter_kws={'s':22})

		# ax.annotate(panel_annot_lst[method_idx * len(prop_lst) + prop_idx], \
		# 			color='k', textcoords='axes fraction', xycoords='axes fraction', \
		# 			fontsize=12, ha='center', xy=(0, 0), xytext=(0.07, 0.88))

	# make legends
	legend_elements = []
	legend_labels = []
	for color, sub_gsc_lst in gsc_color_dict.items():
		group_name = r'$\bf{}$ $\bf{}$'.format(*gsc_group_color_dict[color].split())
		legend_elements.append(Line2D([0], [0], color=color, marker='o', lw=0))
		legend_labels.append(group_name + '\n(' + ', '.join(sub_gsc_lst) + ')')
	fig.legend(legend_elements, legend_labels, ncol=3, loc = 10, \
				bbox_to_anchor=(0.5, 0.03), frameon=False, fontsize=9)

	fig.tight_layout(rect=[0, 0.04, 1, 1])
	plt.subplots_adjust(hspace=0.32, wspace=0.15)
	plt.savefig(fig_dir + figname)
	plt.close()

if __name__ == '__main__':
	result_df = helperfun.get_result_df(result_fp)
	prop_df_dict = helperfun.get_prop_df_dict(prop_dir)
	genfig(result_df, prop_df_dict, 'WebServer_Connectivity.pdf', 'auPRC', 'Holdout', ['SL-A'], 'STRING')




