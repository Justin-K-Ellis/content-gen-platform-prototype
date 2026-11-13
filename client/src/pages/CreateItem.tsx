import { useParams } from "react-router"
import Heading2 from "@/components/Heading2"

export default function CreateItem() {
  const params = useParams()
  const titleText = `Create ${params.itemType?.toUpperCase()} Items`

  return (
    <>
      <header>
        <Heading2 text={titleText} />
      </header>
    </>
  )
}
