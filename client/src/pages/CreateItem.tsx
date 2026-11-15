import { useState } from "react"
import { useParams } from "react-router"
import Heading2 from "@/components/Heading2"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

type Mode = "batch" | "single"

export default function CreateItem() {
  const params = useParams()
  const itemType = params.itemType?.toUpperCase() ?? ""
  const titleText = `Create ${itemType} Items`

  const [mode, setMode] = useState<Mode>("batch")
  const [batchCount, setBatchCount] = useState(3)
  const [prompt, setPrompt] = useState("")
  const [results, setResults] = useState<string[] | null>(null)
  const [isLoading, setIsLoading] = useState(false)

  const handleGenerate = () => {
    setIsLoading(true)
    setTimeout(() => {
      if (mode === "batch") {
        setResults(
          Array.from({ length: batchCount }, (_, i) => `Placeholder ${itemType} item ${i + 1}`)
        )
      } else {
        setResults([`Generated ${itemType} item from prompt: "${prompt}"`])
      }
      setIsLoading(false)
    }, 800)
  }

  const canGenerate = mode === "batch" || prompt.trim().length > 0

  return (
    <>
      <header>
        <Heading2 text={titleText} />
      </header>

      <Card className="mt-6">
        <CardContent className="flex flex-col gap-4">
          <div className="flex gap-2">
            <Button
              variant={mode === "batch" ? "default" : "outline"}
              onClick={() => setMode("batch")}
            >
              Batch
            </Button>
            <Button
              variant={mode === "single" ? "default" : "outline"}
              onClick={() => setMode("single")}
            >
              Single
            </Button>
          </div>

          {mode === "batch" ? (
            <div className="flex flex-col gap-1.5">
              <label htmlFor="batch-count" className="text-sm font-medium">
                Number of items
              </label>
              <Input
                id="batch-count"
                type="number"
                min={1}
                max={10}
                value={batchCount}
                onChange={(e) => setBatchCount(Math.min(10, Math.max(1, Number(e.target.value))))}
                className="w-24"
              />
            </div>
          ) : (
            <div className="flex flex-col gap-1.5">
              <label htmlFor="custom-prompt" className="text-sm font-medium">
                Custom prompt
              </label>
              <Textarea
                id="custom-prompt"
                placeholder={`Describe the ${itemType} item you want to generate...`}
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
              />
            </div>
          )}

          <Button
            className="w-full"
            disabled={isLoading || !canGenerate}
            onClick={handleGenerate}
          >
            {isLoading ? "Generating..." : "Generate"}
          </Button>
        </CardContent>
      </Card>

      {results && (
        <section className="mt-6 flex flex-col gap-3">
          <h3 className="text-lg font-semibold">Results</h3>
          {results.map((result, i) => (
            <Card key={i} size="sm">
              <CardHeader>
                <CardTitle>{result}</CardTitle>
              </CardHeader>
            </Card>
          ))}
        </section>
      )}
    </>
  )
}
