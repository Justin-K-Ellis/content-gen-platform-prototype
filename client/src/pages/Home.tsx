import Heading1 from "@/components/Heading1"
import Heading2 from "@/components/Heading2"
import CardGrid from "@/components/CardGrid"
import { READING_ITEM_TYPES, LISTENING_ITEM_TYPES } from "@/types"
import type { LinkData } from "@/types"

const readingItemData: LinkData[] = READING_ITEM_TYPES.map((item: string) => ({
  text: item,
  url: item.toLowerCase(),
}))

const listeningItemData: LinkData[] = LISTENING_ITEM_TYPES.map(
  (item: string) => ({
    text: item,
    url: item.toLocaleLowerCase(),
  })
)

export default function Home() {
  return (
    <section className="flex flex-col gap-8 p-4">
      <Heading1 text="Item Generator" />
      <div>
        <Heading2 text="Reading" />
        <CardGrid linkData={readingItemData} />
      </div>
      <div>
        <Heading2 text="Listening" />
        <CardGrid linkData={listeningItemData} />
      </div>
    </section>
  )
}
