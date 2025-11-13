import { useState } from "react";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { UploadCloud } from "lucide-react";
import * as pdfjsLib from "pdfjs-dist";

pdfjsLib.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version}/pdf.worker.min.js`;

export default function ComparativoPolitica() {
  const [busca, setBusca] = useState("");
  const [arquivo2025, setArquivo2025] = useState("");
  const [arquivo2026, setArquivo2026] = useState("");
  const [comparativo, setComparativo] = useState([]);

  const handlePDFUpload = async (e, setArquivo) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const fileReader = new FileReader();
    fileReader.onload = async function () {
      const typedArray = new Uint8Array(this.result);
      const pdf = await pdfjsLib.getDocument({ data: typedArray }).promise;
      let text = "";
      for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const content = await page.getTextContent();
        const strings = content.items.map(item => item.str);
        text += strings.join(" ") + " ";
      }
      setArquivo(text);
    };
    fileReader.readAsArrayBuffer(file);
  };

  const compararTextos = () => {
    if (!arquivo2025 || !arquivo2026) return;
    const topicos = ["meta atuarial", "modelo de gestão", "ALM", "governança", "segmentos", "limites", "liquidez", "rentabilidade", "cenário econômico"];
    const resultado = topicos.map(titulo => {
      const trecho2025 = arquivo2025.toLowerCase().includes(titulo) ? titulo : "Não encontrado";
      const trecho2026 = arquivo2026.toLowerCase().includes(titulo) ? titulo : "Não encontrado";
      return {
        titulo: titulo.charAt(0).toUpperCase() + titulo.slice(1),
        atual: trecho2025,
        proposta: trecho2026,
        comentario: trecho2025 === trecho2026 ? "Mantido" : "Possível alteração"
      };
    });
    setComparativo(resultado);
  };

  const dadosFiltrados = comparativo.filter(item =>
    item.titulo.toLowerCase().includes(busca.toLowerCase())
  );

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">Sistema Comparativo: Política de Investimentos</h1>

      <div className="flex gap-4">
        <div className="space-y-2">
          <label className="font-medium">Política 2025 (Atual)</label>
          <input type="file" accept=".pdf" onChange={(e) => handlePDFUpload(e, setArquivo2025)} />
        </div>
        <div className="space-y-2">
          <label className="font-medium">Sugestão Consultoria 2026</label>
          <input type="file" accept=".pdf" onChange={(e) => handlePDFUpload(e, setArquivo2026)} />
        </div>
        <Button onClick={compararTextos}>Comparar Documentos</Button>
      </div>

      <Input
        placeholder="Buscar tópico..."
        value={busca}
        onChange={(e) => setBusca(e.target.value)}
        className="max-w-md"
      />

      <Tabs defaultValue="comparativo">
        <TabsList>
          <TabsTrigger value="comparativo">Comparativo</TabsTrigger>
          <TabsTrigger value="analise">Análise Técnica</TabsTrigger>
          <TabsTrigger value="comentarios">Comentários Estratégicos</TabsTrigger>
        </TabsList>

        <TabsContent value="comparativo">
          <ScrollArea className="h-[500px]">
            {dadosFiltrados.map((item, index) => (
              <Card key={index} className="mb-4">
                <CardContent className="p-4 space-y-2">
                  <h2 className="text-lg font-semibold">{item.titulo}</h2>
                  <div>
                    <strong>2025:</strong> {item.atual}
                  </div>
                  <div>
                    <strong>Proposta 2026:</strong> {item.proposta}
                  </div>
                  <div className="italic text-muted-foreground">{item.comentario}</div>
                </CardContent>
              </Card>
            ))}
          </ScrollArea>
        </TabsContent>

        <TabsContent value="analise">
          <Card>
            <CardContent className="p-4">
              <p>
                O sistema detecta automaticamente os principais tópicos entre os documentos e aponta se há manutenção ou possível alteração com base em palavras-chave estratégicas.
              </p>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="comentarios">
          <Card>
            <CardContent className="p-4">
              <Textarea placeholder="Insira aqui comentários da diretoria ou do comitê..." />
              <Button className="mt-2">Salvar Comentário</Button>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
