# -*- coding: utf-8 -*-
import json

from config import eval_path

if __name__ == '__main__':
    with open(eval_path, 'r', encoding="utf-8") as file:
        eval_result = json.load(file)

    with open('README.t', 'r', encoding="utf-8") as file:
        template = file.readlines()

    template = ''.join(template)

    for i in range(10):
        template = template.replace('$(psnr_{})'.format(i), '{0:.5f} dB'.format(eval_result['psnr_list'][i]))

    template = template.replace('$(avg_psnr)', '{0:.5f}'.format(eval_result['psnr_avg']))

    with open('README.md', 'w', encoding="utf-8") as file:
        file.write(template)
