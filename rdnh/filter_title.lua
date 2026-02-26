local title

-- Promote all headers by one level. Set title from level 1 headers,
-- unless it has been set before.
function promote_header (header)
  if not title and header.level == 1 then
    title = header.content
    return {}
  end
  return header
end

return {
  {Meta = function (meta) title = meta.title end}, -- init title
  {Header = promote_header},
  {Meta = function (meta) meta.title = title; return meta end}, -- set title
}