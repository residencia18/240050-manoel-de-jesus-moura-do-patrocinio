import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'boldText',
  standalone: true
})
export class BoldTextPipe implements PipeTransform {

  transform(text: string, textReceived: string): string {
    if (!textReceived || !text) {
      return text;
    }

    // substituir todas as ocorrências do termo de pesquisa no texto com a versão negritada usando a tag HTML <b>.
    const regex = new RegExp(textReceived, 'gi');
    return text.replace(regex, match => `<b>${match}</b>`);
  }

}
